from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "WebApp/Home.html")


def about(request):
    return render(request, "WebApp/About.html")
