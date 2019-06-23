from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm
from .models import Post
from django.conf import settings

class PostListView(ListView):
    model = Post
    paginate_by = 5
    # context_object_name = 'posts'

    def get_queryset(self):
        # 作成日順に並び替え
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
    f = ContactForm()
    inputDataFromUser=ContactForm(request.POST)
    is_valid = inputDataFromUser.is_valid()
    if is_valid:
        return render(request, 'posts/contact.html', {'contactForm': f})


def emailview(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            # from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER
            to = [settings.EMAIL_HOST_USER]
            try:
                send_mail(subject, message, from_email, to)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "posts/success.html")
    return render(request, "posts/contact.html", {'form': form})


def successview(request):
    return render(request, 'posts/success.html')


def top(request):
    """contact page"""
    return render(request, 'posts/top.html')
