from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class PostAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            title = "Content Title",
            content = "A content body"
        )
    def test_post_list(self):
        response = self.client.get(reverse("post-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)