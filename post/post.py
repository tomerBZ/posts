from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .forms import PostForm
from .serializer import PostSerializer


@api_view(['GET', 'POST', 'DELETE'])
def posts_details(request):

    if request.method == 'POST':
        post_form = PostForm(request.data)
        if post_form.is_valid():
            post_form.save()
            return Response({
                'data': 'success'
            })
        else:
            return Response({
                'data': post_form.errors
            }, status=400)

    if request.method == 'DELETE':
        post = Post.objects.get(pk=request.data['id'])
        post.delete()
        posts = Post.objects.order_by('id')
        serializer = PostSerializer(posts, many=True)
        return Response({
            'data': serializer.data
        })

