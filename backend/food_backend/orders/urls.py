
from django.urls import path
from . import views

urlpatterns = [
    path("", views.order_list),
    path("checkout/", views.checkout_view),
    path("<int:order_id>/", views.order_detail),
    path("<int:order_id>/<str:action>/", views.order_action,),
]
