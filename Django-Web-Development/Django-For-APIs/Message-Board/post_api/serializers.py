from posts.models import Post
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "author", "content")