
from django.db import transaction
from rest_framework.exceptions import ValidationError

from .models import Cart, CartItem
from products.models import Product


def get_customer_cart(user):
    if not hasattr(user, "customer_profile"):
        raise ValidationError(
            "Only customer accounts can use a cart."
        )

    cart, _ = Cart.objects.get_or_create(
        customer=user.customer_profile
    )
    return cart


@transaction.atomic
def add_product_to_cart(user, product_id, quantity, replace_cart=False):
    cart = get_customer_cart(user)

    try:
        product = Product.objects.select_related("seller").get(
            pk=product_id,
            is_available=True,
            seller__is_active=True,
        )
    except Product.DoesNotExist:
        raise ValidationError(
            {"product_id": "This food listing is unavailable."}
        )

    if quantity < 1:
        raise ValidationError(
            {"quantity": "Quantity must be at least 1."}
        )

    if cart.seller_id and cart.seller_id != product.seller_id:
        if not replace_cart:
            raise ValidationError({
                "seller_conflict": (
                    "Your cart contains food from another seller. "
                    "Confirm replacing the cart to continue."
                )
            })

        cart.items.all().delete()
        cart.seller = product.seller
        cart.save(update_fields=["seller", "updated_at"])

    elif cart.seller_id is None:
        cart.seller = product.seller
        cart.save(update_fields=["seller", "updated_at"])

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={"quantity": quantity},
    )

    if not created:
        item.quantity += quantity
        item.save(update_fields=["quantity"])

    return cart


def remove_cart_item(cart, item_id):
    try:
        item = cart.items.get(pk=item_id)
    except CartItem.DoesNotExist:
        raise ValidationError(
            {"item_id": "Cart item not found."}
        )

    item.delete()

    if not cart.items.exists():
        cart.seller = None
        cart.save(update_fields=["seller", "updated_at"])

    return cart
