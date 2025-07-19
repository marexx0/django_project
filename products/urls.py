from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from products import views

urlpatterns = [
    path("", views.index),
    path("list", views.catalog),
    path("delete/<int:id>", views.delete),
    path("create", views.create), 
    path("show/<int:id>", views.show), 
    path("edit/<int:id>", views.edit),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="admin/login.html"), name="login"),
]