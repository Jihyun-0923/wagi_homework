from django.db import models
from django.contrib.auth.models import User  # 기본 User 모델

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ✅ 좋아요 필드 추가 (ManyToMany)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    # ✅ 좋아요 수 반환 메서드
    def total_likes(self):
        return self.likes.count()

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

# ✅ 댓글 모델 추가
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # 어떤 게시글에 달린 댓글인지
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자
    content = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시각

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}'