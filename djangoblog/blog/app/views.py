import markdown
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post

def index(request):
    post_list = Post.objects.all()
    return render(request, 'app/index.html', context = {'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    # 增加markdown依赖
    post.body = markdown.markdown(post.body, extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    return render(request, 'app/detail.html', context = {'post': post})