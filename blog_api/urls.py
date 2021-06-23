""" Define urls """
from django.urls import path
from .views import PostList, PostDetail

APP_NAME = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
]
