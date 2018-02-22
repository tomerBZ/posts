from django.shortcuts import render
from .models import Post


def add_posts_view(request):
    categories = Post.objects.values_list('category', flat=True).distinct()
    return render(request, 'post/post_add.html', {'categories': categories})
