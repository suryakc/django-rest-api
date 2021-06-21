"""
Test the Blog Post API.
"""
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Category

class PostTests(APITestCase):
    """ Test post API"""

    def test_view_posts(self):
        """ Test post get api"""
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        """ Test post create api"""
        test_category = Category.objects.create(name='django')
        self.assertIsNotNone(test_category)
        test_user = User.objects.create_user(username='test', password='test')
        self.assertIsNotNone(test_user)
        post = { "title": "new", "author": 1, "excerpt": "new", "content": "new" }
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, post, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        