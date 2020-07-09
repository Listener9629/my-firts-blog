from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "Web_pageApp/Home.html")


def blog(request):
    return render(request, "Web_pageApp/Blog.html")


def about(request):
    return render(request, "Web_pageApp/About.html")
