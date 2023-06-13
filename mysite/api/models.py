from django.urls import path
from tastypie.resources import ModelResource
from movies.models import Movie
from django.http import Http404
from tastypie.authentication import BasicAuthentication


class MovieResource(ModelResource):
    class Meta:
        authentication = BasicAuthentication()  # Replace with your desired authentication class
        authorization = None
        throttle_class = None
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
    
    def is_authenticated(self, request, **kwargs):
        return True
    
    def prepend_urls(self):
        return [
            # Custom URL for getting a single movie by ID
            path('movies/<int:pk>/', self.wrap_view('get_movie_by_id'),
                 name='api_get_movie_by_id'),
        ]

    def get_movie_by_id(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        movie_id = kwargs.get('pk')
        try:
            movie = Movie.objects.get(id=movie_id)
            bundle = self.build_bundle(obj=movie, request=request)
            data = self.full_dehydrate(bundle)
            return self.create_response(request, data)
        except Movie.DoesNotExist:
            return self.create_response(request, {'error': 'Movie not found'}, Http404)

    def obj_create(self, bundle, **kwargs):
        return super(MovieResource, self).obj_create(bundle, user=bundle.request.user)

    def obj_update(self, bundle, skip_errors=False, **kwargs):
        return super(MovieResource, self).obj_update(bundle, user=bundle.request.user)

    def obj_delete(self, bundle, **kwargs):
        return super(MovieResource, self).obj_delete(bundle, user=bundle.request.user)
