from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all()
    now = datetime.now()
    name = '使用者'
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')