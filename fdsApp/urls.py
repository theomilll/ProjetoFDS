from .views import inventory_list
from django.urls import path


urlpatterns = [
    path("", inventory_list, name="inventory_list"),
]