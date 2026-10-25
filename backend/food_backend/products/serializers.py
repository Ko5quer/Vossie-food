
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    seller_id = serializers.IntegerField(
        source="seller.id",
        read_only=True,
    )
    store_name = serializers.CharField(
        source="seller.store_name",
        read_only=True,
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "seller_id",
            "store_name",
            "name",
            "description",
            "image",
            "price",
            "is_available",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "seller_id",
            "store_name",
            "created_at",
        ]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero."
            )
        return value
