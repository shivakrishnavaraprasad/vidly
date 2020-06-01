from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie
 

# Create your views here.

def index(request):
    movies = Movie.objects.all() 
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    try:
         # we can also use for short version of error handling 
         # movie =get_object_or_404(Movie, id = movie_id)
         # but for now using try and except only 
          
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'movies/detail.html', {'movie': movie})
    except:
        raise Http404()
        