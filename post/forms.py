from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ✅ 게시글 작성용 폼
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # author는 request.user로 자동 설정

# ✅ 회원가입 폼
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# ✅ 댓글 작성용 폼 추가
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']