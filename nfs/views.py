from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.

where = "usa"

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
    return render(request, 'nfs/movie_detail.html', {'movie': movie,'movie_links':base_movie_urls, 'show_links':base_show_urls})

class location(object):
    everything = ""
    action = ""
    adventure = ""
    animation = ""
    comedy = ""
    crime = ""
    documentary = ""
    drama = ""
    family = ""
    fantasy = ""
    history = ""
    horror = ""
    music = ""
    mystery = ""
    romance = ""
    scifi = ""
    sports = ""
    thriller = ""
    war = ""
    western = ""
    reality = ""

    def __init__(self, country, typeOf):
        self.action = country + typeOf + "_action_avg"
        self.adventure = country + typeOf + "_adventure_avg"
        self.animation = country + typeOf + "_anime_avg"
        self.biography = country + typeOf + "_biography_avg"
        self.comedy = country + typeOf + "_comedy_avg"
        self.crime = country + typeOf + "_crime_avg"
        self.documentary = country + typeOf + "_documentary_avg"
        self.drama = country + typeOf + "_drama_avg"
        self.family = country  + typeOf + "_family_avg"
        self.fantasy = country + typeOf + "_fantasy_avg"
        self.history = country + typeOf + "_history_avg"
        self.horror = country  + typeOf + "_horror_avg"
        self.music = country + typeOf + "_music_avg"
        self.mystery = country + typeOf + "_mystery_avg"
        self.romance = country + typeOf + "_romance_avg"
        self.scifi = country + typeOf + "_scifi_avg"
        self.sports = country + typeOf + "_sports_avg"         
        self.thriller = country + typeOf + "_thriller_avg"
        self.war = country + typeOf + "_war_avg"
        self.western = country  + typeOf + "_western_avg"
        self.reality = country + typeOf + "_reality_avg"
        self.everything = country + typeOf + "_all_avg"

base_movie_urls = location("", "movies")
base_show_urls = location("", "shows")


def movies_genre(request, **kwargs):
    country = kwargs.get("kind", None)
    category = kwargs.get("category", None)
    sortBy = kwargs.get("sortBy", None)
    sortClass = ["unsorted", "unsorted", "unsorted", "unsorted"]
    if sortBy == "-tomatoMeter":
        sortClass[0] = "sorted"
    elif sortBy == "-imdbRating":
        sortClass[1] = "sorted"
    elif sortBy == "-Metascore":
        sortClass[2] = "sorted"
    elif sortBy == "-average":
        sortClass[3] = "sorted"
    urlTheme = kwargs.get("urlTheme", None)
    Type = kwargs.get("Type", None)
    global where
    thisPageInfo = pageInfo("movies_" + urlTheme + "_rt", "movies_" + urlTheme +"_imdb", "movies_" + urlTheme + "_mc", "movies_" + urlTheme + "_avg", "Best " + category.title() + " Movies on Netflix Right Now")
    movie_urls = location("", "movies")
    show_urls = location("", "shows")
    if country != "usa":
        where = country + "_"
        movie_urls = location(where, "movies")
        show_urls = location(where, "shows")
        thisPageInfo = pageInfo(country + "_movies_" + urlTheme + "_rt", country + "_movies_" + urlTheme +"_imdb", country + "_movies_" + urlTheme + "_mc", country + "_movies_" + urlTheme + "_avg", "Best " + category.title() + " Movies on Netflix Right Now in " + country.title())
    if category != "all":
        movies = Movie.objects.filter(Genre__contains=category).filter(kind=country).filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type=Type).filter(Genre__contains=category).order_by(sortBy)[:50]
    else:
        movies = Movie.objects.filter(kind=country).filter(tomatoMeter__gte=1).filter(Metascore__gte=1).filter(Type=Type).order_by(sortBy)[:50]
    return render(request, 'nfs/movie_list.html', {'movies': movies, 'pageInfo':thisPageInfo, 'movie_links':movie_urls, 'show_links':show_urls, 'sortClass':sortClass})

def shows_genre(request, **kwargs):
    country = kwargs.get("kind", None)
    category = kwargs.get("category", None)
    sortBy = kwargs.get("sortBy", None)
    sortClass = ["unsorted", "unsorted", "unsorted", "unsorted"]
    if sortBy == "-tomatoMeter":
        sortClass[0] = "sorted"
    elif sortBy == "-imdbRating":
        sortClass[1] = "sorted"
    elif sortBy == "-Metascore":
        sortClass[2] = "sorted"
    elif sortBy == "-average":
        sortClass[3] = "sorted"
    urlTheme = kwargs.get("urlTheme", None)
    Type = kwargs.get("Type", None)
    global where
    thisPageInfo = pageInfo("shows_" + urlTheme + "_rt", "shows_" + urlTheme + "_imdb", "shows_" + urlTheme + "_mc", "shows_" + urlTheme + "_avg", "Best " + category.title() + " Shows on Netflix Now")
    movie_urls = location("", "movies")
    show_urls = location("", "shows")
    if country != "usa":
        where = country + "_"
        movie_urls = location(where, "movies")
        show_urls = location(where, "shows")
        thisPageInfo = pageInfo(country + "_movies_" + urlTheme + "_rt", country + "_movies_" + urlTheme +"_imdb", country + "_movies_" + urlTheme + "_mc", country + "_movies_" + urlTheme + "_avg", "Best " + category.title() + " Movies on Netflix Right Now in " + country.title())
    if category != "all":
        shows = Movie.objects.filter(kind=country).filter(Type=Type).filter(Genre__contains=category).order_by(sortBy)[:50]
    else:
        shows = Movie.objects.filter(kind=country).filter(Type=Type).order_by(sortBy)[:50]
    return render(request, 'nfs/movie_list.html', {'movies': shows, 'pageInfo':thisPageInfo,'movie_links':movie_urls, 'show_links': show_urls, 'sortClass':sortClass})

def about(request):
    return render(request, 'nfs/about.html', {'movie_links':base_movie_urls, 'show_links':base_show_urls})

def privacy(request):
    return render(request, 'nfs/privacy.html', {'movie_links':base_movie_urls, 'show_links':base_show_urls})

def contact(request):
    return render(request, 'nfs/contact.html', {'movie_links':base_movie_urls, 'show_links':base_show_urls})

def countries(request):
    return render(request, 'nfs/countries.html', {'movie_links':base_movie_urls, 'show_links':base_show_urls})
