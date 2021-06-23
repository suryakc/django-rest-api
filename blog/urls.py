""" Define urls """
from django.urls import path
from django.views.generic import TemplateView

app_name = 'blog' # pylint: disable=invalid-name

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
]
