""" API app """
from django.apps import AppConfig

class BlogApiConfig(AppConfig):
    """ API app config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_api'
