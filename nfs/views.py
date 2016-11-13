from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.

class pageInfo(object):
    rturl = ""
    imdburl = ""
    avgurl = ""
    mcurl = ""
    title = ""
    
    def __init__(self, rt, imdb, ms, avg, title):
        self.rturl = rt
        self.imdburl = imdb
        self.mcurl = ms
        self.avgurl = avg
        self.title = title

homePageInfo = pageInfo('movie_list_rt', 'movie_list_imdb', 'movie_list_mc', 'movie_list', "Top Rated Content on Netflix Right Now")

moviePageInfo = pageInfo('movies_main_rt', 'movies_main_imdb', 'movies_main_mc', 'movies_main_avg', 'Best Movies on Netflix')

def movie_list(request):
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).order_by('-average')[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':homePageInfo})

def movie_list_rt(request):
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).order_by('-tomatoMeter')[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':homePageInfo})

def movie_list_imdb(request):
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).order_by('-imdbRating')[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':homePageInfo})

def movie_list_mc(request):
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).order_by('-Metascore')[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':homePageInfo})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'nfs/movie_detail.html', {'movie': movie})

def movies_main_avg(request):
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type='movie').order_by('-average')[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':moviePageInfo})

def movies_main_rt(request):
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type='movie').order_by('-tomatoMeter')[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':moviePageInfo})

def movies_main_imdb(request):
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type='movie').order_by('-imdbRating')[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':moviePageInfo})

def movies_main_mc(request):
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type='movie').order_by('-Metascore')[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':moviePageInfo})

def movies_genre(request, **kwargs):
    category = kwargs.get("category", None)
    sortBy = kwargs.get("sortBy", None)
    urlTheme = kwargs.get("urlTheme", None)
    kind = kwargs.get("kind", None)
    thisPageInfo = pageInfo("movies_" + urlTheme + "_rt", "movies_" + urlTheme +"_imdb", "movies_" + urlTheme + "_mc", "movies_" + urlTheme + "_avg", "Best " + category.title() + " Movies on Netflix Right Now")
    movies = Movie.objects.filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type=kind).filter(Genre__contains=category).order_by(sortBy)[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':thisPageInfo})

def shows_genre(request, **kwargs):
    category = kwargs.get("category", None)
    sortBy = kwargs.get("sortBy", None)
    urlTheme = kwargs.get("urlTheme", None)
    kind = kwargs.get("kind", None)
    thisPageInfo = pageInfo("shows_" + urlTheme + "_rt", "shows_" + urlTheme + "_imdb", "shows_" + urlTheme + "_mc", "shows_" + urlTheme + "_avg", "Best " + category.title() + " Shows on Netflix Now")
    if category != "all":
        shows = Movie.objects.filter(kind=kind).filter(Genre__contains=category).order_by(sortBy)[:50]
    else:
        shows = Movie.objects.filter(kind=kind).order_by(sortBy)[:50]
    return render(request, 'nfs/movie_list.html', {'movies': shows, 'pageInfo':thisPageInfo})

def about(request):
    return render(request, 'nfs/about.html')
