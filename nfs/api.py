from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from nfs.models import Movie

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
        filtering = {
            'category': ALL,
            'kind': ALL,
            'tomatoMeter': ALL,
            'Metascore': ALL,
            'Type': ALL,
            'Genre': ALL,
            'imdbRating': ALL,
            'Title': ALL,
        }
