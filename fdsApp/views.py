from django.shortcuts import render
from .models import fdsApp, computers
from datetime import datetime
import pytz

def inventory_list(request):
    inventories = fdsApp.objects.all()
    inventorypc = computers.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories,
        "inventorypc": inventorypc,
    }
    return render(request, "fds_app/inventory_list.html", context=context)

def horarioDaReservaPC (request):
    timezone = pytz.timezone('America/Sao_Paulo')
    current_datetime = datetime.now(tz = timezone)
    
    dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    str_current_datetime = str(dt)
    
    file_name = str_current_datetime
    file = open("historico.txt", 'a')

    file.write("PC reservado às : \n" + file_name + "\n\n")
    file.close()
    context = {
        "title": "Horário da reserva",
        "file_name": file_name,
    }
    
    return render(request, 'pc1.html', context=context)

def horarioDaReservaLivro (request):
    timezone = pytz.timezone('America/Sao_Paulo')
    current_datetime = datetime.now(tz = timezone)
    
    dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    str_current_datetime = str(dt)
    
    file_name = str_current_datetime
    file = open("historico.txt", 'a')

    file.write("Livro reservado às : \n" + file_name + "\n\n")
    file.close()
    context = {
        "title": "Horário da reserva",
        "file_name": file_name,
    }
    
    return render(request, 'book1.html', context=context)


def book2(request):
    return render(request, 'book2.html')


def pc2(request):
    return render(request, 'pc2.html')
