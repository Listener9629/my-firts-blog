from django.urls import path
from WebApp import views

#Aqui se llaman los templates en views.py la primera parate es el url despues de la direccion del servidor
urlpatterns = [
        path('about/', views.about, name="About"),
]