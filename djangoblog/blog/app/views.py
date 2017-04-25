import markdown
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm


# Create your views here.

from .models import Post, Category

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
    form = CommentForm()
    # 获取这篇post下的所有评论
    comment_list = post.comment_set.all()
    context = {'post': post, 'form': form, 'comment_list': comment_list}
    return render(request, 'app/detail.html', context = context)

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year = year, created_time__month = month)
    return render(request, 'app/index.html', context = {'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk = pk)
    post_list = Post.objects.filter(category = cate)
    return render(request, 'app/index.html', context = {'post_list': post_list})