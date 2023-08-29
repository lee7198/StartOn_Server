from django.db import models

# Create your models here.
from django.db import models

class Top100(models.Model):
    title = models.CharField(max_length=256) # 제목
    artist = models.CharField(max_length=100) # 가수
    genre = models.CharField(max_length=15) # 장르
    image = models.CharField(max_length=256) # 이미지

    def __str__(self):
        return self.title