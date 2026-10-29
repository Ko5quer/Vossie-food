from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("sellers", views.SellerViewSet, basename="seller")
router.register("orders", views.CustomerOrderViewSet, basename="order")
router.register("seller/orders", views.SellerOrderViewSet, basename="seller-order")
router.register("seller/foods", views.SellerFoodViewSet, basename="seller-food")

urlpatterns = [
    path("auth/register/", views.RegisterView.as_view()),
    path("auth/login/", views.LoginView.as_view()),
    path("auth/logout/", views.LogoutView.as_view()),
    path("auth/me/", views.MeView.as_view()),
    path("", include(router.urls)),
]
