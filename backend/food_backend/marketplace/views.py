from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FoodItem, Order, Seller
from .permissions import IsSeller
from .serializers import (
    CheckoutSerializer, CustomerOrderSerializer, FoodSerializer, MeSerializer,
    RegisterSerializer, SellerOrderSerializer, SellerSerializer,
)


# ---------- Auth ----------

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        s = RegisterSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = s.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user": MeSerializer(user).data}, status=201)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = authenticate(
            username=request.data.get("username"), password=request.data.get("password")
        )
        if user is None:
            return Response({"detail": "Wrong username or password."}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user": MeSerializer(user).data})


class LogoutView(APIView):
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(status=204)


class MeView(APIView):
    def get(self, request):
        return Response(MeSerializer(request.user).data)


# ---------- Public catalogue (no login) ----------

class SellerViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = SellerSerializer
    queryset = Seller.objects.filter(is_active=True)

    @action(detail=True, methods=["get"])
    def foods(self, request, pk=None):
        """GET /api/sellers/<id>/foods/ returns only this seller's food."""
        seller = self.get_object()
        foods = seller.foods.filter(is_available=True)
        return Response(FoodSerializer(foods, many=True, context={"request": request}).data)


# ---------- Customer ----------

class CustomerOrderViewSet(viewsets.GenericViewSet,
                           generics.mixins.ListModelMixin,
                           generics.mixins.RetrieveModelMixin):
    """GET /api/orders/ (own orders), POST /api/orders/ (checkout, login required)."""

    serializer_class = CustomerOrderSerializer

    def get_queryset(self):
        return (Order.objects.filter(customer=self.request.user)
                .select_related("seller").prefetch_related("items"))

    def create(self, request):
        s = CheckoutSerializer(data=request.data, context={"request": request})
        s.is_valid(raise_exception=True)
        orders = s.save()
        data = CustomerOrderSerializer(orders, many=True, context={"request": request}).data
        return Response(data, status=status.HTTP_201_CREATED)


# ---------- Seller ----------

class SellerOrderViewSet(viewsets.GenericViewSet,
                         generics.mixins.ListModelMixin,
                         generics.mixins.RetrieveModelMixin):
    permission_classes = [IsSeller]
    serializer_class = SellerOrderSerializer

    def get_queryset(self):
        return (self.request.user.seller_profile.orders
                .prefetch_related("items"))

    def _transition(self, request, pk, from_status, to_status):
        order = get_object_or_404(self.get_queryset(), pk=pk)
        if order.status != from_status:
            return Response(
                {"detail": f"Order is {order.status}, cannot change it this way."}, status=400
            )
        order.status = to_status
        order.save(update_fields=["status", "updated_at"])
        return Response(self.get_serializer(order).data)

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        return self._transition(request, pk, Order.PENDING, Order.APPROVED)

    @action(detail=True, methods=["post"])
    def decline(self, request, pk=None):
        return self._transition(request, pk, Order.PENDING, Order.DECLINED)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        return self._transition(request, pk, Order.APPROVED, Order.COMPLETED)


class SellerFoodViewSet(viewsets.ModelViewSet):
    """Sellers manage only their own food. Use multipart/form-data for the image."""

    permission_classes = [IsSeller]
    serializer_class = FoodSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_queryset(self):
        return self.request.user.seller_profile.foods.all()

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.seller_profile)
