from django import forms
from .models import Post, Comment

# 게시글 작성용 폼
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # author는 request.user로 자동 설정

# 댓글 작성용 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']