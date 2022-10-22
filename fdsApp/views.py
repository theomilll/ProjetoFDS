from django.shortcuts import render
from .models import fdsApp

def inventory_list(request):
    inventories = fdsApp.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request, "fds_app/inventory_list.html", context=context)

def book1(request):
    return render(request, 'book1.html')