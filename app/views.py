from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import PostForm,ReviewForm
from .models import Post, Review
from django.http import HttpResponseRedirect

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


def review(request,id):
    all_reviews = Review.get_reviews(id)
    image = get_object_or_404(Post, id=id)
    form = ReviewForm(request.POST)
    if form.is_valid():
            review = form.save(commit=False)
            review.post = image
            review.user = request.user.profile
            review.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ReviewForm()
    return render(request, 'reviews.html', {"reviews":all_reviews, "form":form})
