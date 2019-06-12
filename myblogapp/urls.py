"""myblogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path, re_path, reverse_lazy
from django.contrib import admin
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.shortcuts import resolve_url
from django.contrib.syndication.views import Feed

from django.conf.urls.static import static
from django.conf import settings
from posts import views
from django.conf.urls import url
from posts.models import *
from posts import urls



class IndexSitemap(Sitemap):
    # サイトマップの「changefreq」・「priority」タグに何を出力するかを決めます。
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        # return resolve_url('post_detail', pk=obj.pk)
        return resolve_url('posts:index')

    def lastmod(self, obj):
        return obj.published


sitemaps = {
    'posts': IndexSitemap,
}


class LatestPostFeed(Feed):
    title = "Okada's blog new posts"
    link = reverse_lazy('posts:index')
    description = "New article from Okada's blog"

    def items(self):
        return Post.objects.order_by('-published')[:9]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:50]  # 本文の20文字目までをとりあえず説明に。

    def item_link(self, item):
        return resolve_url('posts:index')

    def item_image(self, item):
        return item.image



urlpatterns = [
    # path('<url>', views, nickname) nicknames allow us to chane URLs without worrying rewriting urlpatterns
    # path('__debug__/', include(debug_toolbar.urls)),
path('', views.top, name='top'),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('latest/feed/', LatestPostFeed()),
    path('', views.top, name='top'),
]

urlpatterns += i18n_patterns(
   path('', include('posts.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)