from django.db import models
from django.urls import reverse_lazy
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("posts:post-detail", kwargs={"pk": self.id})