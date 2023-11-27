from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]

    context = {'posts': posts}
    return render(request, 'portfolio_app/index.html', context)

def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts': posts}
    return render(request, 'portfolio_app/posts.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}

    return render(request, 'portfolio_app/post.html', context)

def profile(request):
    return render(request, 'portfolio_app/profile.html')

