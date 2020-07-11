from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "WebApp/Home.html")


def blog(request):
    return render(request, "WebApp/Blog.html")


def about(request):
    return render(request, "WebApp/About.html")
