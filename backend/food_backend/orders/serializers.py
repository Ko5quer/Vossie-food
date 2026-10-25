
from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "product_name",
            "unit_price",
            "quantity",
            "subtotal",
        ]

    def get_subtotal(self, obj):
        return obj.unit_price * obj.quantity


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    seller_name = serializers.CharField(
        source="seller.store_name",
        read_only=True,
    )
    customer_email = serializers.EmailField(
        source="customer.user.email",
        read_only=True,
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "customer",
            "customer_email",
            "seller",
            "seller_name",
            "items",
            "status",
            "payment_status",
            "total",
            "created_at",
        ]
        read_only_fields = fields
