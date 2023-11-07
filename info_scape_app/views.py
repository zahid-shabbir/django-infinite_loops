from datetime import date
from django.shortcuts import render, get_list_or_404
from .models import Post


def home(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'info_scape_app/index.html', {'posts': latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'info_scape_app/all-posts.html', {'posts': all_posts})


def post_detail(request, slug):
    identified_post = get_list_or_404(Post, slug=slug)
    identified_post = identified_post[0]
    tags = identified_post.tags.all()
    return render(request, 'info_scape_app/post-detail.html', {'post': identified_post, 'tags': tags},)
