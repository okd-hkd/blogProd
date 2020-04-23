from django.urls import path, include, re_path
from posts.views import PostListView, emailview, successview
from django.views.generic.base import TemplateView

from posts.models import Post
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    re_path(r'(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('contact/', views.emailview, name='email'),
    path('success/', views.successview, name='success'),
    path('search-result/', views.searchlistview, name='search-result'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt',content_type="text/plain")),
    #  {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    path('', views.top, name='top'),
    # path('contact/', views.contact, name='contact'),
]
