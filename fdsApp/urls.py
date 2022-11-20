from .views import inventory_list, reserve_book, return_book, reserve_computer, free_computer
from django.urls import path

urlpatterns = [
    path("", inventory_list, name="inventory_list"),
    path("reserve/book/<int:id>/", reserve_book, name="reserve_book"),
    path("return/book/<int:id>/", return_book, name="return_book"),
    path("reserve/computer/<int:id>/", reserve_computer, name="reserve_computer"),
    path("free/computer/<int:id>/", free_computer, name="free_compute"),

]
