from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("movies/", movie_list, name="movies-list"),
    path("movies/<int:pk>/", movie_detail, name="movies-detail")
]

app_name = "cinema"