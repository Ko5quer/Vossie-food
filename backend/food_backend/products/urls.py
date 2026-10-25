
from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list_create),
    path("<int:product_id>/", views.product_detail),
]
