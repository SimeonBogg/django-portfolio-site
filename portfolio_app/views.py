from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

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


#CRUD Views Below
@login_required(login_url="home")
def createPost(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'portfolio_app/post_form.html', context)


@login_required(login_url="home")
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'portfolio_app/post_form.html', context)


@login_required(login_url="home")
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'item':post}
    return render(request, 'portfolio_app/delete.html', context)
