from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import PostForm

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
    form_class = PostForm

    def form_valid(self, form):
        form_instance = form.save(commit=False)
        form_instance.author = self.request.user
        form_instance = form.save()
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post-update.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post-delete.html"
    success_url = reverse_lazy("posts:post-list")
