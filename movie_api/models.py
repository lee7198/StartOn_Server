from django.db import models

class Movie(models.Model):
    movie_cd = models.CharField(max_length=10)
    movie_nm = models.CharField(max_length=200)
    genre_nm = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=300, default='/default.jpeg')

    def __str__(self):
        return self.movie_nm
