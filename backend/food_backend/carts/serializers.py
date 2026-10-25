
from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "subtotal"]

    def get_subtotal(self, obj):
        return obj.product.price * obj.quantity


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    seller_id = serializers.IntegerField(read_only=True)
    seller_name = serializers.CharField(
        source="seller.store_name",
        read_only=True,
        allow_null=True,
    )
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "id", "seller_id", "seller_name",
            "items", "total", "updated_at",
        ]

    def get_total(self, obj):
        return sum(
            (item.product.price * item.quantity
             for item in obj.items.select_related("product").all()),
            start=0,
        )
