""" Models for our Blog """
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    """ Category definition """
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    """ Blog Post definition """
    class PostObjects(models.Manager): # pylint: disable=too-few-public-methods
        """ object collection for published posts """
        def get_queryset(self):
            """ get filtered posts (published) """
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')

    objects = models.Manager()
    postobjects = PostObjects()

    class Meta: # pylint: disable=too-few-public-methods
        """ Meta info"""
        ordering = ('-published',)

    def __str__(self) -> str:
        return str(self.title)
