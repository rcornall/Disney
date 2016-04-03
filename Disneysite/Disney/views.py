from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Movie


def index(request):
    movie_list = Movie.objects.order_by('-year')
    context = {
        'movie_list': movie_list,
        'col_loop': range(1,3),
    }
    return render(request, 'Disney/index.html', context)
