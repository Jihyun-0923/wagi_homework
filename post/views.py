from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, PostImage, Comment
from .forms import PostForm, CommentForm

# 게시글 목록
def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'posts': posts})

# 게시글 상세 (댓글 기능 포함)
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post:detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

# 좋아요 토글 (로그인 필요)
@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post:detail', post_id=post.id)

# 게시글 작성 (로그인 필요)
@login_required
def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            # 다중 이미지 저장
            for f in request.FILES.getlist('images'):
                PostImage.objects.create(post=post, image=f)

            return redirect('post:detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'write.html', {'form': form})

# 게시글 수정 (로그인 + 본인만 가능 + 이미지 삭제/추가)
@login_required
def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        return redirect('post:detail', post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = post.author  # 작성자 유지
            updated_post.save()

            # 선택된 이미지 삭제
            delete_ids = request.POST.getlist('delete_images')
            for image_id in delete_ids:
                image = PostImage.objects.filter(id=image_id, post=post).first()
                if image:
                    image.delete()

            # 새 이미지 추가
            for f in request.FILES.getlist('images'):
                PostImage.objects.create(post=post, image=f)

            return redirect('post:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    existing_images = post.images.all()

    return render(request, 'write.html', {
        'form': form,
        'is_edit': True,
        'existing_images': existing_images,
        'post': post,
    })

# 검색 기능
def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_result.html', {'results': results, 'query': query})