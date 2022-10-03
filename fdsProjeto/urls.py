from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory/", include("fdsApp.urls")),
    path("", auth_views.LoginView.as_view(template_name = "inventory_system/login.html"), name="login")
]
