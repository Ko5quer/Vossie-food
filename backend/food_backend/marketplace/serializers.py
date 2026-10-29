from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers

from .models import CustomerProfile, FoodItem, Order, OrderItem, Seller

User = get_user_model()


# ---------- Public catalogue ----------

class FoodSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FoodItem
        fields = ["id", "seller", "name", "description", "price", "image", "is_available"]


class SellerSerializer(serializers.ModelSerializer):
    """Public view of a seller. Phone is deliberately NOT included."""

    class Meta:
        model = Seller
        fields = ["id", "name", "faculty", "description", "profile_pic"]


# ---------- Auth ----------

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=60)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=30)

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("That username is taken.")
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, data):
        phone = data.pop("phone")
        user = User.objects.create_user(**data)
        CustomerProfile.objects.create(user=user, phone=phone)
        return user


class MeSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    seller_id = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "email", "phone", "role", "seller_id"]

    def get_role(self, user):
        return "seller" if hasattr(user, "seller_profile") else "customer"

    def get_seller_id(self, user):
        return user.seller_profile.pk if hasattr(user, "seller_profile") else None

    def get_phone(self, user):
        profile = getattr(user, "customer_profile", None)
        return profile.phone if profile else ""


# ---------- Orders ----------

class OrderItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "food", "name", "unit_price", "quantity", "subtotal"]


class CheckoutItemSerializer(serializers.Serializer):
    food = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1, max_value=99)


class CheckoutSerializer(serializers.Serializer):
    """Cart lives in React. It is sent here as a list of {food, quantity}."""

    items = CheckoutItemSerializer(many=True, allow_empty=False)
    contact_name = serializers.CharField(max_length=120)
    contact_phone = serializers.CharField(max_length=30)
    delivery_address = serializers.CharField(max_length=255)
    note = serializers.CharField(required=False, allow_blank=True, default="")

    def validate_items(self, items):
        # merge duplicate lines
        merged = {}
        for i in items:
            merged[i["food"]] = merged.get(i["food"], 0) + i["quantity"]
        foods = {
            f.pk: f
            for f in FoodItem.objects.filter(
                pk__in=merged.keys(), is_available=True, seller__is_active=True
            ).select_related("seller")
        }
        missing = set(merged) - set(foods)
        if missing:
            raise serializers.ValidationError(
                f"These items are no longer available: {sorted(missing)}"
            )
        return [(foods[pk], qty) for pk, qty in merged.items()]

    @transaction.atomic
    def create(self, data):
        user = self.context["request"].user
        items = data.pop("items")
        by_seller = {}
        for food, qty in items:
            by_seller.setdefault(food.seller, []).append((food, qty))
        orders = []
        for seller, lines in by_seller.items():  # one order per seller
            order = Order.objects.create(customer=user, seller=seller, **data)
            OrderItem.objects.bulk_create(
                OrderItem(order=order, food=f, name=f.name, unit_price=f.price, quantity=q)
                for f, q in lines
            )
            orders.append(order)
        return orders


class CustomerOrderSerializer(serializers.ModelSerializer):
    """What the customer sees. Seller phone only after approval."""

    items = OrderItemSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    seller = SellerSerializer(read_only=True)
    seller_contact = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id", "status", "status_display", "payment_method", "seller", "seller_contact",
            "contact_name", "contact_phone", "delivery_address", "note",
            "items", "total", "created_at",
        ]

    def get_seller_contact(self, order):
        if not order.contact_shared:
            return None
        return {"name": order.seller.name, "phone": order.seller.phone}


class SellerOrderSerializer(serializers.ModelSerializer):
    """What the seller sees. Customer details only after approval."""

    items = OrderItemSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    customer_contact = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id", "status", "status_display", "payment_method",
            "customer_contact", "items", "total", "created_at",
        ]

    def get_customer_contact(self, order):
        if not order.contact_shared:
            return None
        return {
            "name": order.contact_name,
            "phone": order.contact_phone,
            "address": order.delivery_address,
            "note": order.note,
        }
