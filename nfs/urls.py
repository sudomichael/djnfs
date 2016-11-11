from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.movie_list, name='movie_list'),
    url(r'^movie/(?P<pk>\d+)/$', views.movie_detail, name='movie_detail'),
    url(r'^tomatosort$', views.movie_list_rt, name="movie_list_rt"),
    url(r'^imdbsort$', views.movie_list_imdb, name="movie_list_imdb"),
    url(r'^mcsort$', views.movie_list_mc, name="movie_list_mc"),
]
