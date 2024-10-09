from django.shortcuts import render


# Create your views here.
# Aqui se traen los templates (html) para seguir llamandolos en urls.py

def about(request):
    return render(request, "WebApp/About.html")
