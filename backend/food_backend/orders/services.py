
from decimal import Decimal

from django.db import transaction
from rest_framework.exceptions import ValidationError

from carts.models import Cart
from orders.models import Order, OrderItem


@transaction.atomic
def checkout(user):
    if not hasattr(user, "customer_profile"):
        raise ValidationError(
            "Only customer accounts can place orders."
        )

    try:
        cart = Cart.objects.select_for_update().get(
            customer=user.customer_profile
        )
    except Cart.DoesNotExist:
        raise ValidationError("Your cart is empty.")

    items = list(
        cart.items.select_related(
            "product",
            "product__seller",
        ).all()
    )

    if not items:
        raise ValidationError("Your cart is empty.")

    if cart.seller is None or not cart.seller.is_active:
        raise ValidationError(
            "The seller is no longer available."
        )

    total = Decimal("0.00")

    for item in items:
        product = item.product

        if not product.is_available:
            raise ValidationError(
                f"{product.name} is no longer available."
            )

        if product.seller_id != cart.seller_id:
            raise ValidationError(
                "Your cart contains food from different sellers."
            )

        total += product.price * item.quantity

    order = Order.objects.create(
        customer=user.customer_profile,
        seller=cart.seller,
        total=total,
        status=Order.Status.PENDING,
        payment_status=Order.PaymentStatus.UNPAID,
    )

    OrderItem.objects.bulk_create([
        OrderItem(
            order=order,
            product=item.product,
            product_name=item.product.name,
            unit_price=item.product.price,
            quantity=item.quantity,
        )
        for item in items
    ])

    cart.items.all().delete()
    cart.seller = None
    cart.save(update_fields=["seller", "updated_at"])

    return order
