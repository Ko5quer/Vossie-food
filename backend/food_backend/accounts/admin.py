from django.contrib import admin
from .models import CustomerProfile, SellerProfile

# Register your models here.

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    search_fields = ("user__username", "user__email")


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "store_name", "user", "is_active")
    list_filter = ("is_active",)
    search_fields = (
        "store_name",
        "user__username",
        "user__email",
    )
