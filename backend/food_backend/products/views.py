from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import (api_view, permission_classes, parser_classes,)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# Create your views here.


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def product_list_create(request):
    if request.method == "GET":
        products = Product.objects.filter(
            is_available=True,
            seller__is_active=True,
        ).select_related("seller")

        serializer = ProductSerializer(
            products,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    if not request.user.is_authenticated:
        return Response(
            {"error": "Authentication required."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    try:
        seller = request.user.seller_profile
    except Exception:
        return Response(
            {"error": "Only seller accounts can list food."},
            status=status.HTTP_403_FORBIDDEN,
        )

    if not seller.is_active:
        return Response(
            {"error": "This seller account is inactive."},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = ProductSerializer(
        data=request.data,
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    product = serializer.save(seller=seller)

    return Response(
        ProductSerializer(
            product,
            context={"request": request},
        ).data,
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def product_detail(request, product_id):
    product = get_object_or_404(
        Product.objects.select_related("seller"),
        pk=product_id,
    )

    if request.method == "GET":
        if not product.is_available:
            return Response(
                {"error": "Food listing not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            ProductSerializer(
                product,
                context={"request": request},
            ).data
        )

    if not request.user.is_authenticated:
        return Response(
            {"error": "Authentication required."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    if not hasattr(request.user, "seller_profile"):
        return Response(
            {"error": "Only sellers can manage food listings."},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.user.seller_profile.id != product.seller_id:
        return Response(
            {"error": "You cannot manage another seller's listing."},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "PATCH":
        serializer = ProductSerializer(
            product,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    # Soft-delete: keep historical order references intact.
    product.is_available = False
    product.save(update_fields=["is_available"])

    return Response(status=status.HTTP_204_NO_CONTENT)
