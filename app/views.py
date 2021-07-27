from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import PostForm
from .models import Post


# Create your views here.
def welcome(request):
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    form = PostForm(request.POST or None, files=request.FILES)      
    if form.is_valid():
        post=form.save(commit=False)
        post.user = request.user.profile
        post.save()
        return redirect('home')
    context = {
        'posts': posts,
        'form': form,
        'users':users,
    }
    # users = Profile.objects.all()
    return render(request, 'index.html',context)

def upload_image(request):
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    form = PostForm(request.POST or None, files=request.FILES)      
    if form.is_valid():
        post=form.save(commit=False)
        post.user = request.user.profile
        post.save()
        return redirect('index')
    context = {
        'posts': posts,
        'form': form,
        'users':users,
    }
    return render(request,'create_post.html',{"form":form})
