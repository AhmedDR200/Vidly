from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.



def index(request):
    # select * from movies_movie
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies':movies})
