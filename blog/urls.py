""" Define urls """
from django.urls import path
from django.views.generic import TemplateView

APP_NAME = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
]
