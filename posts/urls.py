from django.urls import path, include, re_path
from posts.views import PostListView, emailview, successview

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
    path('', views.top, name='top'),
    # path('contact/', views.contact, name='contact'),
]
