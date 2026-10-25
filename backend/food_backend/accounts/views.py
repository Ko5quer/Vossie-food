from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import (api_view, permission_classes,)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import (CustomerRegistrationSerializer,SellerRegistrationSerializer,)


# Create your views here.


def account_response(user):
    if hasattr(user, "seller_profile"):
        role = "SELLER"
        profile = {
            "store_name": user.seller_profile.store_name,
        }
    elif hasattr(user, "customer_profile"):
        role = "CUSTOMER"
        profile = {}
    else:
        role = "ADMIN" if user.is_staff else "UNKNOWN"
        profile = {}

    token, _ = Token.objects.get_or_create(user=user)

    return {
        "token": token.key,
        "user": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": role,
            **profile,
        },
    }


@api_view(["POST"])
@permission_classes([AllowAny])
@transaction.atomic
def register_customer(request):
    serializer = CustomerRegistrationSerializer(
        data=request.data
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    return Response(
        account_response(user),
        status=status.HTTP_201_CREATED,
    )


@api_view(["POST"])
@permission_classes([AllowAny])
@transaction.atomic
def register_seller(request):
    serializer = SellerRegistrationSerializer(
        data=request.data
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    return Response(
        account_response(user),
        status=status.HTTP_201_CREATED,
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email", "").strip().lower()
    password = request.data.get("password", "")

    if not email or not password:
        return Response(
            {"error": "Email and password are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = authenticate(
        request,
        username=email,
        password=password,
    )

    if user is None or not user.is_active:
        return Response(
            {"error": "Invalid email or password."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    return Response(account_response(user))


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    # Token logout invalidates the current token.
    request.auth.delete()

    return Response(
        {"message": "Logged out successfully."},
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user

    if hasattr(user, "seller_profile"):
        role = "SELLER"
        profile = {
            "store_name": user.seller_profile.store_name,
        }
    elif hasattr(user, "customer_profile"):
        role = "CUSTOMER"
        profile = {}
    else:
        role = "ADMIN" if user.is_staff else "UNKNOWN"
        profile = {}

    return Response({
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": role,
        **profile,
    })
