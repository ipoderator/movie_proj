from django.shortcuts import render,get_object_or_404
from .models import Movie
from django.db.models import F,Sum,Max,Min,Count,Avg


def show_all_movie(request):
    movies = Movie.objects.order_by('name', 'badget')
    agg = movies.aggregate(Avg('badget'),Max('rating'), Min('year'), Count('id'))
    return render(request, 'movie_app/all_movie.html', {
      'movies' : movies,  
      'agg': agg,
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
      'movie' : movie  
    })
