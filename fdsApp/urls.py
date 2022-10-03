from django.urls import path
from .views import inventory_list

urlpatterns = [
    path("", inventory_list, name="inventory_list")
]
