from django.contrib import admin
from .models import Article,Comment

class CommentStackedInline(admin.StackedInline):
    model = Comment
    extra = 3

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'added_by', 'date_published', 'status']
    prepopulated_fields = {'slug':('title',)}
    inlines = [CommentStackedInline]


admin.site.register(Comment)

