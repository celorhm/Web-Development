from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import BookForm
from .models import Book
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView

# Create your views here.
class BookCreateView(CreateView):
    form_class = BookForm
    model = Book
    template_name = 'book/add_book.html'

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'

