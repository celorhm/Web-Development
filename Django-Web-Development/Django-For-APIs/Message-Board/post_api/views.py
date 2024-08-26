from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from posts.models import Post
from rest_framework.permissions import IsAdminUser
from .permissions import IsAuthororReadOnly

# Create your views here.
class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthororReadOnly]

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthororReadOnly]