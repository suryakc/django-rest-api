""" View definitions """
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """ Post List """
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    """ Post Details """
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
