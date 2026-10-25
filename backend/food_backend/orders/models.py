from django.db import models
from accounts.models import CustomerProfile, SellerProfile
from products.models import Product

# Create your models here.



class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending seller confirmation"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"
        READY = "READY", "Ready for collection"
        COLLECTED = "COLLECTED", "Collected"
        CANCELLED = "CANCELLED", "Cancelled"

    class PaymentStatus(models.TextChoices):
        UNPAID = "UNPAID", "Unpaid"
        PAID = "PAID", "Paid"

    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.PROTECT,
        related_name="orders",
    )
    seller = models.ForeignKey(
        SellerProfile,
        on_delete=models.PROTECT,
        related_name="orders",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    payment_status = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID,
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    product_name = models.CharField(max_length=150)
    unit_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    quantity = models.PositiveIntegerField()

    @property
    def subtotal(self):
        return self.unit_price * self.quantity
