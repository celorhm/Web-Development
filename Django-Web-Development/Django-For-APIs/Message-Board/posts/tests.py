from django.test import TestCase,SimpleTestCase
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class PostsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username="test user")
        cls.post = Post.objects.create(title="Test", content="This is test data", author=cls.author)
    
    def test_post_model(self):
        self.assertEqual(self.post.content, "This is test data") #test the content of the model object
        self.assertEqual(self.post.author.username, "test user") #test the username of the model object
        self.assertEqual(str(self.post), "Test")
    
    def test_model_list(self):
        path_response = self.assertEqual(self.client.get("/").status_code, 200)
        url_name_response = self.assertEqual(self.client.get(reverse("post-list")).status_code, 200)
        template_response =self.assertTemplateUsed(self.client.get("/"), "posts/post-list.html")
        return True
    
    
    def test_model_detail(self):
        response = self.client.get("/post/1/")
        url_path_response = self.assertEqual(response.status_code, 200)
        url_name_response = self.assertEqual((self.client.get(reverse("post-detail", kwargs={"pk": self.post.id}))).status_code, 200)
        first_data = self.assertTemplateUsed(response, "posts/post-detail.html")
        return True
    

    def test_model_create(self):
        response = self.client.post(
            reverse("post-create"), {"title": "This You", "body": "You were the one that brought this up", "author": self.author.id },
        )
        self.assertEqual(response.status_code, 200)

    
    def test_model_update(self):
        response = self.client.post(
            reverse("post-update", args="1"), {"title": "Updated title", "body": "Update text"},
        )
        self.assertEqual(response.status_code, 200)
    
    def test_post_deleteview(self):
        response = self.client.post(reverse("post-delete", args="1"))
        self.assertEqual(response.status_code, 302)

