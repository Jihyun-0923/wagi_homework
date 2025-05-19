from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # user/views.py에 register 함수 있다고 가정

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),  # 회원가입
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # 로그인
    path('logout/', auth_views.LogoutView.as_view(next_page='user:login'), name='logout'),   # 로그아웃
]
