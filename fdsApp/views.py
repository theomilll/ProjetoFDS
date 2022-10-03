from django.shortcuts import render

def index(request):
    context = {
        "title": "Index Page"
    }
    return render(request, "fds_app/index.html", context=context)