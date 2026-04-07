from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Post

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')

    return render(request, 'signup.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            slug=request.POST['slug']
        )
        return redirect('home')

    return render(request, 'add_post.html')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})