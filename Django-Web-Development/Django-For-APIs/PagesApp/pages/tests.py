from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class HomepageTest(SimpleTestCase):
    def test_url_path(self):
        response = self.client.get("/")
        return self.assertEqual(response.status_code, 200)
    def test_url_name(self):
        response = self.client.get(reverse("home"))
        return self.assertEqual(response.status_code, 200)
    def test_url_template_name(self):
        response = self.client.get(reverse("about"))
        return self.assertTemplateUsed(response, "pages/about.html")
    def test_url_template_contents(self):
        response = self.client.get(reverse("home"))
        return self.assertContains(response, "<h2>Welcome</h2>")
    

class AboutpageTest(SimpleTestCase):
    def test_url_name(self):
        response = self.client.get(reverse("about"))
        return self.assertEqual(response.status_code, 200)
    def test_url_path(self):
        response = self.client.get("/about/")
        return self.assertEqual(response.status_code,200)
    def test_template_name(self):
        response = self.client.get(reverse("about"))
        return self.assertTemplateUsed(response, "pages/about.html")
    def test_template_contains(self):
        response = self.client.get(reverse("about"))
        return self.assertContains(response, "<h2>About Page</h2>")