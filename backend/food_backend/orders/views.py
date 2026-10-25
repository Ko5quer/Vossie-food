from django.db.models import Prefetch
from rest_framework import status
from rest_framework.decorators import ( api_view, permission_classes,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Order, OrderItem
from .serializers import OrderSerializer
from .services import checkout

# Create your views here.




def order_queryset():
    return Order.objects.select_related(
        "customer__user",
        "seller",
    ).prefetch_related(
        Prefetch(
            "items",
            queryset=OrderItem.objects.select_related("product"),
        )
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def checkout_view(request):
    try:
        order = checkout(request.user)
    except ValidationError as exc:
        return Response(
            {"error": exc.detail},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response(
        OrderSerializer(order).data,
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_list(request):
    if hasattr(request.user, "seller_profile"):
        orders = order_queryset().filter(
            seller=request.user.seller_profile
        )
    elif hasattr(request.user, "customer_profile"):
        orders = order_queryset().filter(
            customer=request.user.customer_profile
        )
    else:
        return Response(
            {"error": "This account cannot access marketplace orders."},
            status=status.HTTP_403_FORBIDDEN,
        )

    return Response(OrderSerializer(orders, many=True).data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_detail(request, order_id):
    orders = order_queryset()

    if hasattr(request.user, "seller_profile"):
        orders = orders.filter(seller=request.user.seller_profile)
    elif hasattr(request.user, "customer_profile"):
        orders = orders.filter(customer=request.user.customer_profile)
    else:
        return Response(
            {"error": "This account cannot access marketplace orders."},
            status=status.HTTP_403_FORBIDDEN,
        )

    order = orders.filter(pk=order_id).first()

    if order is None:
        return Response(
            {"error": "Order not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    return Response(OrderSerializer(order).data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def order_action(request, order_id, action):
    # Only the seller assigned to the order can manage fulfilment.
    if not hasattr(request.user, "seller_profile"):
        if action == "cancel" and hasattr(
            request.user, "customer_profile"
        ):
            order = Order.objects.filter(
                pk=order_id,
                customer=request.user.customer_profile,
            ).first()

            if order is None:
                return Response(
                    {"error": "Order not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            if order.status != Order.Status.PENDING:
                return Response(
                    {"error": "Only pending orders can be cancelled."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            order.status = Order.Status.CANCELLED
            order.save(update_fields=["status"])

            return Response(OrderSerializer(order).data)

        return Response(
            {"error": "Only the assigned seller can perform this action."},
            status=status.HTTP_403_FORBIDDEN,
        )

    order = order_queryset().filter(
        pk=order_id,
        seller=request.user.seller_profile,
    ).first()

    if order is None:
        return Response(
            {"error": "Order not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    transitions = {
        "accept": (Order.Status.PENDING, Order.Status.ACCEPTED),
        "reject": (Order.Status.PENDING, Order.Status.REJECTED),
        "ready": (Order.Status.ACCEPTED, Order.Status.READY),
        "collect": (Order.Status.READY, Order.Status.COLLECTED),
    }

    if action not in transitions:
        return Response(
            {"error": "Unknown order action."},
            status=status.HTTP_404_NOT_FOUND,
        )

    expected_status, new_status = transitions[action]

    if order.status != expected_status:
        return Response(
            {
                "error": (
                    f"Cannot {action} an order with status "
                    f"{order.status}."
                )
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    order.status = new_status
    update_fields = ["status"]

    if action == "collect":
        order.payment_status = Order.PaymentStatus.PAID
        update_fields.append("payment_status")

    order.save(update_fields=update_fields)

    return Response(OrderSerializer(order).data)
