from django.contrib import admin
from .models import Post, PostImage

# ✅ PostImage를 Post 안에서 관리할 수 있도록 Inline 정의
class PostImageInline(admin.TabularInline):  # 또는 StackedInline 써도 돼
    model = PostImage
    extra = 1  # 이미지 입력 칸 몇 개 보일지

# ✅ Post 등록할 때 이미지도 같이 관리할 수 있도록 설정
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ('title', 'author', 'created_at')  # 관리자 목록에 보여줄 항목

# ✅ PostImage도 독립적으로 관리할 수 있도록 (선택사항)
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')