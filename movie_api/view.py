from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import Movie
from rest_framework.decorators import api_view
import requests

# API 키를 `settings.py` 파일에서 가져옵니다.
from django.conf import settings

def search_movie_poster(movie_title):
    # 검색 API 호출 및 데이터 추출
    search_api_key = "7b8701345172f46cdefd221a2adf3926"  # 실제 API 키로 대체
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={search_api_key}&query={movie_title}"

    response = requests.get(search_url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            poster_path = results[0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

@api_view(['GET'])
def get_movie_info(request):
    # API를 호출하여 데이터를 가져옵니다.
    response = requests.get("https://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={key}".format(key=settings.KOBIS_API_KEY))

    # 응답이 정상이면 데이터를 추출합니다.
    if response.status_code == 200:
        movie_list = response.json()["movieListResult"]["movieList"]

        for movie_data in movie_list:
            movie, created = Movie.objects.get_or_create(
                movie_cd=movie_data["movieCd"],
                defaults={
                    "movie_nm": movie_data["movieNm"],
                    "genre_nm": movie_data["repGenreNm"]
                }
            )

        try: 
            if created or not movie.poster_url:
                print(f"영화 '{movie.movie_nm}'의 포스터 이미지가 저장되었습니다.")
                poster_url = search_movie_poster(movie.movie_nm)
                if poster_url:
                    movie.poster_url = poster_url
                    movie.save()
                    print(f"영화 '{movie.movie_nm}'의 포스터 이미지가 저장되었습니다.")
                else:
                    print(f"영화 '{movie.movie_nm}'의 포스터 이미지 저장에 실패했습니다.")
            else:
                print(f'{movie.movie_nm}, {movie.genre_nm}, {movie.poster_url}')

        except Exception as e:
            print(e)

        return JsonResponse({
            "message": "영화 정보와 포스터 이미지가 저장되었습니다."
        })

    # 응답이 정상이 아니면 에러를 반환합니다.
    else:
        return JsonResponse({
            "error": "API 호출에 실패했습니다."
        })
    
