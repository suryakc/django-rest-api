from os import name
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        test_category = Category.objects.create(name='django')
        test_user = User.objects.create_user(username='test_user', password='123456789')
        test_post = Post.objects.create(category_id=1, title='post title', excerpt='post excerpt',
            content='test content', slug='post title', author_id=1, status='published')
    
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)
        self.assertEqual(f'{post.author}', 'test_user')
        self.assertEqual(f'{post.title}', 'post title')
        self.assertEqual(f'{post.excerpt}', 'post excerpt')
        self.assertEqual(f'{post.content}', 'test content')
        self.assertEqual(f'{post.slug}', 'post title')
        self.assertEqual(f'{post.status}', 'published')
        self.assertEqual(str(post), 'post title')
        self.assertEqual(str(category), 'django')