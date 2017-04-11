from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from nfs.models import Movie

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
        filtering = {
            'Title': ALL,
            'Year': ALL,
            'Runtime': ALL,
            'Genre': ALL,
            'Director': ALL,
            'Actors': ALL,
            'imdbRating': ALL,
            'Type': ALL,
            'Poster': ALL,
            'tomatoConsensus': ALL,
            'tomatoMeter': ALL,
            'Metascore': ALL,
            'Website': ALL,
            'Plot': ALL,
            'Language': ALL,
            'Metascore': ALL,
            'Type': ALL, 
            'tomatoUserRating': ALL,
            'tomatoFresh': ALL,
            'totalSeasons': ALL,
            'tomatoRating': ALL,
            'imdbID': ALL,
            'Country': ALL,
            'Writer': ALL,
            'Rated': ALL,
            'average': ALL,
            'kind': ALL,
 }
