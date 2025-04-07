from django.urls import path
from .views import list, detail, write

app_name = 'post'  

urlpatterns = [
    path('', list, name='list'),  # 홈 (게시글 목록)
    path('write/', write, name='write'),  # 글 작성
    path('<int:post_id>/', detail, name='detail'),  # 상세 페이지 (detail 앞에 'detail/' 제거)
]