from django.db import models
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=200, default="")
    text = models.TextField(default="")
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title
