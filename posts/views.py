from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator


class PostListView(ListView):
    model = Post
    paginate_by = 3
    # context_object_name = 'posts'

    def get_queryset(self):
        # 公開フラグがTrueで、作成日順に並び替え
        return super().get_queryset().order_by('-published')


"""
def index(request):
    # return HttpResponse("Hello World! このページは投稿のインデックスです。")
    postsPub = Post.objects.order_by('-published')
    paginator = Paginator(postsPub, 5)  # Show 5 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'posts/index.html', {'posts': posts})
"""


def post_detail(request, post_id):
    """detail page"""
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


def about(request):
    """about page"""
    return render(request, 'posts/about.html')


def contact(request):
    """contact page"""
    return render(request, 'posts/contact.html')
