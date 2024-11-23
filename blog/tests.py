from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secretpassword123",
        )

        cls.post = Post.objects.create(
            title="A good title",
            body="Creating nice body for you",
            author=cls.user,
        )

        def test_post_model(self):
            self.assertEqual(self.post.title, "A good title")
            self.assertEqual(self.post.body, "Creating a nice body for you")
            self.assertEqual(self.post.author.username, "testuser")
            self.assertEqual(str(self.post), "A good title")
            self.assertEqual(self.post.get_absolute_url(), "/post/1/")
