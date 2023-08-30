from django.db import models

# Create your models here.
class Mbti(models.Model):
    mbti = models.TextField()
    Percent = models.FloatField()