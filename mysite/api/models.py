from tastypie.resources import ModelResource
from tastypie import fields
from movies.models import Movie, Genre


class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'


class MovieResource(ModelResource):
    genre = fields.ForeignKey(GenreResource, 'genre', full=True)

    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'

    def determine_format(self, request):
        fmt = super(MovieResource, self).determine_format(request)

        if fmt == 'text/html':
            return 'application/json'

        return fmt

    def dispatch(self, request_type, request, **kwargs):
        # Allow DELETE requests sent from forms
        if request_type == 'DELETE' and 'HTTP_X_METHODOVERRIDE' in request.META:
            request_type = 'DELETE'

        return super(MovieResource, self).dispatch(request_type, request, **kwargs)
