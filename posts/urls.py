from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from posts import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('post.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': False, }),
]
