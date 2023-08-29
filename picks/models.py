from django.db import models

# Create your models here.
class Top100(models.Model):
    artist = models.CharField(max_length=100) # 가수
    genre = models.CharField(max_length=50) # 장르
    image = models.CharField(max_length=256) # 이미지
    title = models.CharField(max_length=256) # 제목

    def __str__(self):
        return self.title