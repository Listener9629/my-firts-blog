from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "WebApp/Home.html")


def about(request):
    return render(request, "WebApp/About.html")
