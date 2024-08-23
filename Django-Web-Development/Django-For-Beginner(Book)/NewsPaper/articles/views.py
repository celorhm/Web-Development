from django.shortcuts import render,get_list_or_404
from .models import Article
from django.views.generic import ListView,DetailView,View
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import CommentForm


# Create your views here.
class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/article-list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = Article.objects.filter(status=Article.Status.PUBLISHED)
        return queryset
# CommentsView
class CommentGetView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article/article-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["comment_form"] = CommentForm()
        return context
     
class CommentPostView(SingleObjectMixin,FormView):
   form_class = CommentForm
   model = Article
   template_name = 'article/article-detail.html'

   def post(self, request, *args, **kwargs):
       self.object = self.get_object()
       return super().post(request, *args, **kwargs)
   
   def form_valid(self, form):
       comment = form.save(commit=False)
       comment.article = self.object
       comment.added_by = self.request.user
       comment = form.save()
       return super().form_valid(form)
   
   def get_success_url(self):
       article = self.get_object()
       return reverse_lazy("articles:article-detail", kwargs={"pk": article.id})

class ArticleDetailView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        view = CommentGetView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPostView.as_view()
        return view(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article/article-create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        article = form.save(commit=False)
        article.added_by = self.request.user
        article = form.save()
        return super().form_valid(form)
    

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    template_name = 'article/article-update.html'
    fields = ['content']

    def test_func(self):
        article = self.get_object()
        return article


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article/article-delete.html'
    success_url = reverse_lazy("articles:article-list")




    
        


   