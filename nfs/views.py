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

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'nfs/movie_detail.html', {'movie': movie})

def movies_genre(request, **kwargs):
    country = kwargs.get("kind", None)
    category = kwargs.get("category", None)
    sortBy = kwargs.get("sortBy", None)
    urlTheme = kwargs.get("urlTheme", None)
    Type = kwargs.get("Type", None)
    thisPageInfo = pageInfo("movies_" + urlTheme + "_rt", "movies_" + urlTheme +"_imdb", "movies_" + urlTheme + "_mc", "movies_" + urlTheme + "_avg", "Best " + category.title() + " Movies on Netflix Right Now")
    if country != "usa":
        thisPageInfo = pageInfo(country + "_movies_" + urlTheme + "_rt", country + "_movies_" + urlTheme +"_imdb", country + "_movies_" + urlTheme + "_mc", country + "_movies_" + urlTheme + "_avg", "Best " + category.title() + " Movies on Netflix Right Now in " + country.title())
    if category != "all":
        movies = Movie.objects.filter(Genre__contains=category).filter(kind=country).filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type=Type).filter(Genre__contains=category).order_by(sortBy)[:50]
    else:
        movies = Movie.objects.filter(kind=country).filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type=Type).order_by(sortBy)[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':thisPageInfo})

def shows_genre(request, **kwargs):
    country = kwargs.get("kind", None)
    category = kwargs.get("category", None)
    sortBy = kwargs.get("sortBy", None)
    urlTheme = kwargs.get("urlTheme", None)
    Type = kwargs.get("Type", None)
    thisPageInfo = pageInfo("shows_" + urlTheme + "_rt", "shows_" + urlTheme + "_imdb", "shows_" + urlTheme + "_mc", "shows_" + urlTheme + "_avg", "Best " + category.title() + " Shows on Netflix Now")
    if country != "usa":
        thisPageInfo = pageInfo(country + "_movies_" + urlTheme + "_rt", country + "_movies_" + urlTheme +"_imdb", country + "_movies_" + urlTheme + "_mc", country + "_movies_" + urlTheme + "_avg", "Best " + category.title() + " Movies on Netflix Right Now in " + country.title())
    if category != "all":
        shows = Movie.objects.filter(kind=country).filter(Type=Type).filter(Genre__contains=category).order_by(sortBy)[:50]
    else:
        shows = Movie.objects.filter(kind=country).filter(Type=Type).order_by(sortBy)[:50]
    return render(request, 'nfs/movie_list.html', {'movies': shows, 'pageInfo':thisPageInfo})

def about(request):
    return render(request, 'nfs/about.html')

def privacy(request):
    return render(request, 'nfs/privacy.html')

def contact(request):
    return render(request, 'nfs/contact.html')

def countries(request):
    return render(request, 'nfs/countries.html')
