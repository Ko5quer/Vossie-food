from rest_framework import status
from rest_framework.decorators import ( api_view, permission_classes,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import CartItem
from .serializers import CartSerializer
from .services import (get_customer_cart, add_product_to_cart, remove_cart_item,)


# Create your views here.


@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated])
def cart_detail(request):
    cart = get_customer_cart(request.user)

    if request.method == "GET":
        return Response(
            CartSerializer(cart).data
        )

    cart.items.all().delete()
    cart.seller = None
    cart.save(update_fields=["seller", "updated_at"])

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cart_add_item(request):
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity", 1)
    replace_cart = request.data.get("replace_cart", False)

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        return Response(
            {"quantity": "Enter a whole number."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not isinstance(replace_cart, bool):
        return Response(
            {"replace_cart": "Enter true or false."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if product_id is None:
        return Response(
            {"product_id": "This field is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        cart = add_product_to_cart(
            request.user,
            product_id,
            quantity,
            replace_cart,
        )
    except ValidationError as exc:
        message = exc.detail
        code = (
            status.HTTP_409_CONFLICT
            if isinstance(message, dict)
            and "seller_conflict" in message
            else status.HTTP_400_BAD_REQUEST
        )
        return Response(message, status=code)

    return Response(
        CartSerializer(cart).data,
        status=status.HTTP_200_OK,
    )


@api_view(["PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def cart_item_detail(request, item_id):
    cart = get_customer_cart(request.user)

    try:
        item = cart.items.select_related(
            "product", "product__seller"
        ).get(pk=item_id)
    except CartItem.DoesNotExist:
        return Response(
            {"error": "Cart item not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "DELETE":
        remove_cart_item(cart, item_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    quantity = request.data.get("quantity")

    if (
        isinstance(quantity, bool)
        or not isinstance(quantity, int)
        or quantity < 1
    ):
        return Response(
            {"quantity": "Enter a whole number of at least 1."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if (
        not item.product.is_available
        or not item.product.seller.is_active
    ):
        return Response(
            {"error": "This food listing is no longer available."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    item.quantity = quantity
    item.save(update_fields=["quantity"])

    return Response(CartSerializer(cart).data)
