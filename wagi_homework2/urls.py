"""
URL configuration for wagi_homework2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from post.views import register  # 회원가입 뷰 import

urlpatterns = [
    path('admin/', admin.site.urls),

    # 기본 경로 접근 시 로그인 페이지로 리디렉션
    path('', lambda request: redirect('login')),

    # 게시글 관련 URL들 (post 앱)
    path('post/', include(('post.urls', 'post'), namespace='post')),

    # 로그인 / 로그아웃 / 회원가입
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/register/', register, name='register'),
]

# 개발환경에서 media 파일 처리
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)