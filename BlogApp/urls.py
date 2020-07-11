from django.urls import path
from BlogApp.views import PublisherList

urlpatterns = [
    path('blog-prueba/', PublisherList.as_view(), name="Blog"),
]
