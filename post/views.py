from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def list(request):
    posts = Post.objects.all().order_by('-created_at')  
    return render(request, 'list.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})

def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post:list')  
    else:
        form = PostForm()
    return render(request, 'write.html', {'form': form})