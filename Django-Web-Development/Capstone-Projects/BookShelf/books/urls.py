from django.urls import path
from .views import BookListView,BookCreateView,BookDetailView

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("create/", BookCreateView.as_view(), name="create-book")
]
