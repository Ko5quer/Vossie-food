from decimal import Decimal

from django.conf import settings
from django.db import models


class Seller(models.Model):
    """A food seller. Created by you in Django admin.

    Link `user` to a Django user if you want the seller to log in and
    manage orders from the seller dashboard.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="seller_profile",
        help_text="Login account for this seller (optional).",
    )
    name = models.CharField(max_length=120)
    faculty = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="sellers/", blank=True, null=True)
    phone = models.CharField(
        max_length=30, blank=True,
        help_text="Private. Only shown to a customer once the seller approves their order.",
    )
    is_active = models.BooleanField(default=True, help_text="Untick to hide from the site.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="foods")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="foods/", blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.seller})"


class CustomerProfile(models.Model):
    """Extra details for customers. Contact info is only shown to a seller
    once they approve that customer's order."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_profile"
    )
    phone = models.CharField(max_length=30)
    default_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Profile of {self.user}"


class Order(models.Model):
    PENDING, APPROVED, DECLINED, COMPLETED = "pending", "approved", "declined", "completed"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (DECLINED, "Declined"),
        (COMPLETED, "Completed"),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=PENDING)
    payment_method = models.CharField(max_length=30, default="Cash on delivery", editable=False)
    # Snapshot of contact details at the time of ordering
    contact_name = models.CharField(max_length=120)
    contact_phone = models.CharField(max_length=30)
    delivery_address = models.CharField(max_length=255)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.pk} for {self.seller}"

    @property
    def total(self):
        return sum((i.subtotal for i in self.items.all()), Decimal("0.00"))

    @property
    def contact_shared(self):
        """Once approved, seller and customer can see each other's contact details."""
        return self.status in (self.APPROVED, self.COMPLETED)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    food = models.ForeignKey(FoodItem, on_delete=models.SET_NULL, null=True, blank=True)
    # Snapshots so old orders stay correct if a food is edited or deleted
    name = models.CharField(max_length=120)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.name}"
