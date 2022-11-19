from django.shortcuts import render
from .models import fdsApp, computers

def inventory_list(request):
    inventories = fdsApp.objects.all()
    inventorypc = computers.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories,
        "inventorypc": inventorypc,
    }
    return render(request, "fds_app/inventory_list.html", context=context)

#def pc_list(request):
    inventorypc = computers.objects.all()
    context = {
        "title": "Inventory List PC",
        "inventorypc": inventorypc
    }
    return render(request, "fds_app/inventory_list.html", context=context)
    

def book1(request):
    return render(request, 'book1.html')


def book2(request):
    return render(request, 'book2.html')


def pc1(request):
    return render(request, 'pc1.html')


def pc2(request):
    return render(request, 'pc2.html')
