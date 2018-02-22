from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializer import PostSerializer
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination


class PostsList(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self):
        posts = Post.objects.order_by('-id').all()
        return posts
