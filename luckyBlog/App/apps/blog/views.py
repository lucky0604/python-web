# @Author: lucky
# @Date:   2017-04-25T23:45:55+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-29T23:49:54+08:00



from django.shortcuts import render, HttpResponse
from pure_pagination import Paginator, PageNotAnInteger
from django.views.generic import View
from django.db.models import Q
from .models import *
from .forms import *
from users.models import Comment, Reply
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.

__all__ = [
    'ArticleListView',
    'ArticleDetailView',
    'CommentsView',
    'ReplyView',
    'AboutView'
]

class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.filter(status = 0).order_by('-created_time')
        search = request.GET.get('search')
        search_sm = request.GET.get('search_sm')
        if search:
            articles = articles.filter(Q(title__icontains = search) | Q(body__icontains = search))
        if search_sm:
            articles = articles.filter(Q(title__icontains = search_sm) | Q(body__icontains = search_sm))
        tag = request.GET.get('tag')
        categories = request.GET.get('category')
        if tag:
            T = Tag.objects.get(name = tag)
            articles = articles.filter(tag = T)

        if categories:
            C = Categories.objects.get(name = categories)
            articles = articles.filter(categories = C)

        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 10, request = request)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)

        comments = Comment.objects.all().order_by('-add_time')[:5]
        links = Link.objects.all()
        categories = Categories.objects.all()
        tags = Tag.objects.all()
        reads = Article.objects.all().order_by('-read')[:5]
        try:
            setting = Setting.objects.get(pk = 1)
        except Setting.DoesNotExist:
            setting = None
        return render(request, 'index.html', {'articles': articles,
        'comments': comments,
        'links': links,
        'categories': categories,
        'tags': tags,
        'reads': reads,
        'setting': setting})

class ArticleDetailView(View):
    pass

class CommentsView(View):
    pass

class ReplyView(View):
    pass

class AboutView(View):
    pass
