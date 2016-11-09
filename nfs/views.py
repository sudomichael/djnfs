from django.shortcuts import render
from .models import Movie
# Create your views here.

def movie_list(request):
    movies = Movie.objects.filter(tomatoMeter__gte=90).order_by('-tomatoMeter')
    return render(request, 'nfs/movie_list.html', {'movies': movies})


