from rest_framework.permissions import BasePermission


class IsSeller(BasePermission):
    """Logged-in user who has a Seller profile attached (set up in admin)."""

    message = "This account is not linked to a seller."

    def has_permission(self, request, view):
        u = request.user
        return bool(u and u.is_authenticated and hasattr(u, "seller_profile"))
