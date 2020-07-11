from django.urls import path
from BlogApp.views import PublisherList

urlpatterns = [
    path('blog/', PublisherList.as_view(), name="Blog"),
]
