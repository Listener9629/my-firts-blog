from django.shortcuts import render
from django.views.generic import ListView
from BlogApp.models import Blog


# Create your views here.

class PublisherList(ListView):
    model = Blog
