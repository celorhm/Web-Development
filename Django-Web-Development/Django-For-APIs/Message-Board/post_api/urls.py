from django.urls import path
from .views import PostListAPIView,PostDetailAPIView

app_name = 'post_api'
urlpatterns = [
    path("", PostListAPIView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail")
]
