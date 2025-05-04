from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, PostImage
from .forms import PostForm, RegisterForm

# 게시글 목록
def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'posts': posts})

# 게시글 상세
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'post': post})

# 게시글 작성 (로그인 필요)
@login_required
def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 로그인한 사용자로 작성자 설정
            post.save()

            # 다중 이미지 저장
            for f in request.FILES.getlist('images'):
                PostImage.objects.create(post=post, image=f)

            return redirect('post:detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'write.html', {'form': form})

# 게시글 수정 (로그인 + 본인만 가능)
@login_required
def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 본인만 수정 가능
    if request.user != post.author:
        return redirect('post:detail', post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = post.author  # 작성자 변경 방지
            updated_post.save()
            return redirect('post:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'write.html', {'form': form, 'is_edit': True})

# 회원가입 → 가입 후 로그인 페이지로 이동
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # 사용자 생성
            return redirect('login')  # 로그인 페이지로 이동
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})