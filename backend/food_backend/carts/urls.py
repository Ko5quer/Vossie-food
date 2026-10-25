
from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_detail),
    path("items/", views.cart_add_item),
    path("items/<int:item_id>/", views.cart_item_detail),
]
