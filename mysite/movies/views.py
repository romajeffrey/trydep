from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
# def index(request):
#     return HttpResponse("Hello word")

def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.name for m in movies])
        # return render(request, 'index.html', {'movies': movies})
    # return HttpResponse("Hello word")
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):

    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
