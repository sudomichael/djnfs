from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from nfs.models import Movie

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
