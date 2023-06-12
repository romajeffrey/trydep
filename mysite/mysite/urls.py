from django.contrib import admin
from django.urls import path, include

from api.models import MovieResource
# from . import views

movie_resource = MovieResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include("movies.urls")),
    path('api/', include(movie_resource.urls))
]
