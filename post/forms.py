from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ✅ 게시글 작성용 폼
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # ❌ author 제거 (자동 할당되기 때문)

# ✅ 회원가입 폼
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']