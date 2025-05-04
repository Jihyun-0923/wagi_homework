from django.urls import path
from .views import list, detail, write, edit, register
from django.contrib.auth import views as auth_views

app_name = 'post'

urlpatterns = [
    # 게시판 기능
    path('', list, name='list'),                        # 게시글 목록
    path('write/', write, name='write'),                # 글 작성
    path('<int:post_id>/', detail, name='detail'),      # 게시글 상세
    path('<int:post_id>/edit/', edit, name='edit'),     # 글 수정

    # 회원 관련 기능
    path('register/', register, name='register'),       # 회원가입
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # 로그인
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),        # 로그아웃
]