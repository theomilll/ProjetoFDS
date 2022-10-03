from django.shortcuts import render

def index(request):
    return render(request, "fds_app/index.html")