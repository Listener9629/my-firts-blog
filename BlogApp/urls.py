from django.urls import path
from BlogApp.views import PublisherList

urlpatterns = [
    path('', PublisherList.as_view(), name="Blog"),
]
