from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.movie_list, name='movie_list'),
    url(r'^movie/(?P<pk>\d+)/$', views.movie_detail, name='movie_detail'),
    url(r'^tomatosort$', views.movie_list_rt, name="movie_list_rt"),
    url(r'^imdbsort$', views.movie_list_imdb, name="movie_list_imdb"),
    url(r'^mcsort$', views.movie_list_mc, name="movie_list_mc"),
    url(r'^netflixmovies/all$', views.movies_main_avg, name="movies_main_avg"),
    url(r'^netflixmovies/tomatosort$', views.movies_main_rt, name="movies_main_rt"),
    url(r'^netflixmovies/imdbsort$', views.movies_main_imdb, name="movies_main_imdb"),
    url(r'^netflixmovies/mcsort$', views.movies_main_mc, name="movies_main_mc"),
    url(r'^netflixactionmovies$', views.movies_action_avg, name="movies_action_avg"),
]
