# title, year, runtime, genre, director, actors, imdbRating, rated
# poster, type, tomatoConsensus, tomatoMeter, avg, website, plot

from django.db import models
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=6)
    runtime = models.CharField(max_length=20)
    genre = models.CharField()
    director = models.CharField()
    actors = models.TextField()
    imdbRating = models.CharField()
    rated = models.CharField()
    Poster = models.TextField()
    movType = models.CharField()
    tomatoConsensus = models.TextField()
    tomatoMeter = models.CharField()
    avg = models.CharField()
    website = models.TextField()
    plot = models.TextField()
    Error = models.TextField()
    Response = models.TextField()
    
    def __str__(self):
        return self.title
