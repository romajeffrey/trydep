from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource
from . import views

from rest_framework import routers
from api2.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

movie_resource = MovieResource()

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('movies/', include("movies.urls")),
    path('api/', include(movie_resource.urls)),
    # path('api2/', include("api2.urls")),
    path('todos/', include(router.urls)),

]
