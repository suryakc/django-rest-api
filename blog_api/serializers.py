""" Serializers """
from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    """ Blog Post serializer """
    class Meta: # pylint: disable=too-few-public-methods
        """ Meta data """
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status', 'category')
