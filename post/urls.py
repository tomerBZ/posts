from . import views
from . import add_view
from django.conf.urls import url
from post.post import posts_details
from post.list import PostsList

urlpatterns = [
    url(r'^$', views.posts_view, name='posts_view'),
    url(r'^add', add_view.add_posts_view, name='post_add_view'),
    url(r'^post/list', PostsList.as_view(), name='posts_list_page'),
    url(r'^post/', posts_details, name='posts_list'),
]
