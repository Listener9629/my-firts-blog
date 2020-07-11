from django.urls import path
from WebApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('blog/', views.blog, name="Blog"),
    path('about/', views.about, name="About"),
]