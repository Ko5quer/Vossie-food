
from django.urls import path
from . import views

urlpatterns = [
    path("register/customer/", views.register_customer),
    path("login/", views.login),
    path("logout/", views.logout),
    path("me/", views.me),
]
