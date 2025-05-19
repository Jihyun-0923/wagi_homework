from django.urls import path
from .views import list, detail, write, edit, toggle_like, search  # ✅ register는 제거!

app_name = 'post'

urlpatterns = [
    # 게시판 기능
    path('', list, name='list'),
    path('write/', write, name='write'),
    path('<int:post_id>/', detail, name='detail'),
    path('<int:post_id>/edit/', edit, name='edit'),
    path('<int:post_id>/like/', toggle_like, name='toggle_like'),

    # 검색 기능
    path('search/', search, name='search'),
]