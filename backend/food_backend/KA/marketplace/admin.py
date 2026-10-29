from django.contrib import admin

from .models import CustomerProfile, FoodItem, Order, OrderItem, Seller


class FoodInline(admin.TabularInline):
    model = FoodItem
    extra = 1


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("name", "faculty", "phone", "user", "is_active")
    list_filter = ("faculty", "is_active")
    search_fields = ("name", "faculty")
    inlines = [FoodInline]


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("name", "seller", "price", "is_available")
    list_filter = ("seller", "is_available")
    search_fields = ("name",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("food", "name", "unit_price", "quantity")
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "seller", "customer", "status", "created_at")
    list_filter = ("status", "seller")
    inlines = [OrderItemInline]
    actions = ["approve", "decline", "complete"]

    @admin.action(description="Approve selected orders")
    def approve(self, request, queryset):
        queryset.filter(status=Order.PENDING).update(status=Order.APPROVED)

    @admin.action(description="Decline selected orders")
    def decline(self, request, queryset):
        queryset.filter(status=Order.PENDING).update(status=Order.DECLINED)

    @admin.action(description="Mark selected orders completed")
    def complete(self, request, queryset):
        queryset.filter(status=Order.APPROVED).update(status=Order.COMPLETED)


admin.site.register(CustomerProfile)
