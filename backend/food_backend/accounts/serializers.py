
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import CustomerProfile, SellerProfile

User = get_user_model()


class CustomerRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    def validate_email(self, value):
        value = value.strip().lower()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                "An account with this email already exists."
            )
        return value

    def create(self, validated_data):
        email = validated_data["email"]

        user = User.objects.create_user(
            username=email,
            email=email,
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        CustomerProfile.objects.create(user=user)
        return user


class SellerRegistrationSerializer(CustomerRegistrationSerializer):
    store_name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        store_name = validated_data.pop("store_name")
        email = validated_data["email"]

        user = User.objects.create_user(
            username=email,
            email=email,
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        SellerProfile.objects.create(
            user=user,
            store_name=store_name,
        )
        return user
