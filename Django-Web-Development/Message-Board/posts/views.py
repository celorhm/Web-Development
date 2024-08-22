from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/post-list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post-detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post-create.html'
    fields = ['title', 'content' , 'author']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post-update.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post-delete.html"
    success_url = reverse_lazy("post-list")
