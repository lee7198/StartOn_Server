from django.urls import path
from .view import get_movie_info

urlpatterns = [
    path("get_movie_info/", get_movie_info),
]
