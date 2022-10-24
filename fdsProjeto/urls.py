from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from fdsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory/", include("fdsApp.urls")),
    path("", auth_views.LoginView.as_view(template_name = "inventory_system/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "inventory_system/logout.html"), name="logout"),
    path("inventory/book1/", views.book1, name="book1"),
    path("inventory/book2/", views.book2, name="book2"),
    path("inventory/pc1/", views.pc1, name="pc1"),
    path("inventory/pc2/", views.pc2, name="pc2")
] 