from django.shortcuts import render
from .models import Post


def posts_view(request):
    return render(request, 'post/post_list.html')


def posts_view_static(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list_static.html',  {'posts': posts})
