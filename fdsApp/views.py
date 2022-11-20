from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewUserForm
from .models import fdsApp, computers
from datetime import datetime
import pytz


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("inventory_list")
        else:
            return render(request=request, template_name="inventory_system/register.html",
                          context={"register_form": form})

    form = NewUserForm()
    return render(request=request, template_name="inventory_system/register.html", context={"register_form": form})


def inventory_list(request, book_id=None):
    inventories = fdsApp.objects.all()
    inventorypc = computers.objects.all()

    context = {
        "title": "Inventory List",
        "inventories": inventories,
        "inventorypc": inventorypc,
    }
    return render(request, "fds_app/inventory_list.html", context=context)


def horarioDaReservaPC(request):
    timezone = pytz.timezone('America/Sao_Paulo')
    current_datetime = datetime.now(tz=timezone)

    dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    str_current_datetime = str(dt)

    file_name = str_current_datetime
    file = open("historico.txt", 'a')

    file.write("PC reservado as : \n" + file_name + "\n\n")
    file.close()
    context = {
        "title": "Horário da reserva",
        "file_name": file_name,
    }

    return render(request, 'pc1.html', context=context)


def horarioDaReservaLivro(request):
    timezone = pytz.timezone('America/Sao_Paulo')
    current_datetime = datetime.now(tz=timezone)

    dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    str_current_datetime = str(dt)

    file_name = str_current_datetime
    file = open("historico.txt", 'a')

    file.write("Livro reservado as : \n" + file_name + "\n\n")
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


def reserve_book(request, id):
    timezone = pytz.timezone('America/Sao_Paulo')
    current_datetime = datetime.now(tz=timezone)

    dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    str_current_datetime = str(dt)

    file_name = str_current_datetime
    file = open("historico.txt", 'a')

    file.write("Livro reservado as : \n" + file_name + "\n\n")
    file.close()
    
    book_object = get_object_or_404(fdsApp, id=id)
    book_object.quantity_in_stock -= 1
    book_object.save()
    return redirect('inventory_list')


def return_book(request, id):
    timezone = pytz.timezone('America/Sao_Paulo')
    current_datetime = datetime.now(tz=timezone)

    dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    str_current_datetime = str(dt)

    file_name = str_current_datetime
    file = open("historico.txt", 'a')

    file.write("O Livro devolvido as : \n" + file_name + "\n\n")
    file.close()
    
    book_object = get_object_or_404(fdsApp, id=id)
    book_object.quantity_in_stock += 1
    book_object.save()

    return redirect('inventory_list')


def reserve_computer(request, id):
    timezone = pytz.timezone('America/Sao_Paulo')
    current_datetime = datetime.now(tz=timezone)

    dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    str_current_datetime = str(dt)

    file_name = str_current_datetime
    file = open("historico.txt", 'a')

    file.write("PC reservado as : \n" + file_name + "\n\n")
    file.close()
    computer_object = get_object_or_404(computers, id=id)
    computer_object.c_quantity_in_stock -= 1
    computer_object.save()
    return redirect('inventory_list')


def free_computer(request, id):
    timezone = pytz.timezone('America/Sao_Paulo')
    current_datetime = datetime.now(tz=timezone)

    dt = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    str_current_datetime = str(dt)

    file_name = str_current_datetime
    file = open("historico.txt", 'a')

    file.write("O PC foi devolvido as : \n" + file_name + "\n\n")
    file.close()
    computer_object = get_object_or_404(computers, id=id)
    computer_object.c_quantity_in_stock += 1
    computer_object.save()

    return redirect('inventory_list')
