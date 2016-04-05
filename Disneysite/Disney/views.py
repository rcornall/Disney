from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import Http404

from .models import Movie


def index(request):
    movie_list = Movie.objects.order_by('-year')
    context = {
        'movie_list': movie_list,
    }
    return render(request, 'Disney/index.html', context)


def movie(request, _title):
    movie = get_object_or_404(Movie, title=_title)
    context = {
        'movie': movie,
    }
    return render(request, 'Disney/movie.html', context)
