from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    post_list = Post.objects.all()
    return render(request, 'app/index.html', context = {'post_list': post_list})
