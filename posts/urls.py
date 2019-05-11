from django.urls import path, include, re_path
from posts.views import PostListView

from posts.models import Post
from . import views

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    re_path(r'(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
   ]


# urlpatterns += i18n_patterns(
#     path('about/', about_views.main, name='about'),
#     path('news/', include(news_patterns, namespace='news')),
# 　　
