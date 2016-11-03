from django.db import models
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=6)
    runtime = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.TextField()
    imdbRating = models.CharField(max_length=10)
    rated = models.CharField(max_length=10)
    poster = models.TextField()
    movType = models.CharField(max_length=30)
    tomatoConsensus = models.TextField()
    tomatoMeter = models.CharField(max_length=10)
    avg = models.CharField(max_length=10)
    website = models.TextField()
    plot = models.TextField()

    def __str__(self):
        return self.title                     
