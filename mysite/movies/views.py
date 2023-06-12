from django.http import HttpResponse
from django.shortcuts import render
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

