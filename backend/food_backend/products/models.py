from django.db import models
from accounts.models import SellerProfile

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(
        SellerProfile,
        on_delete=models.PROTECT,
        related_name="products",
    )
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="food/")
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
