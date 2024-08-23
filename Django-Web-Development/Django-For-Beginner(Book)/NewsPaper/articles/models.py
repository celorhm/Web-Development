from django.db import models
from django.urls import reverse_lazy
from django.conf import settings

# Create your models here.
class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices, max_length=255, default=Status.DRAFT)

    class Meta:
        ordering = ['date_published']
        indexes = [models.Index(fields=['-date_published']),]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("articles:article-detail", kwargs={"pk": self.id})
    

class Comment(models.Model):
    comment = models.TextField()
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    class Meta:
        ordering = ['date_added']

    