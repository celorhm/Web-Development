from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    class Status(models.TextChoices):
        to_read = ("to read", "To Read")
        on_going = ("on going", "ON Going")
        completed = ("completed", "Completed")
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_started = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    status = models.CharField(choices=Status.choices, max_length=255, default=Status.to_read)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book", kwargs={"pk": self.pk})

class BookSummary(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    summary_title = models.CharField(max_length=255,null=True, blank=True)
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.book
    
    def get_absolute_url(self):
        return reverse("summary", kwargs={"pk": self.pk})