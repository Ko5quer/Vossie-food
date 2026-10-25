from django.db import models
from accounts.models import CustomerProfile, SellerProfile
from products.models import Product

# Create your models here.

class Cart(models.Model):
    customer = models.OneToOneField(
        CustomerProfile,
        on_delete=models.CASCADE,
        related_name="cart",
    )
    seller = models.ForeignKey(
        SellerProfile,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="carts",
    )
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["cart", "product"],
                name="unique_product_per_cart",
            ),
            models.CheckConstraint(
                condition=models.Q(quantity__gte=1),
                name="cart_item_quantity_at_least_one",
            ),
        ]
