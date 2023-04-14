from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


def create(request):
    return


def detail(request, pk):
    return


def update(request, pk):
    return


def delete(request, pk):
    return


def comments_create(request, pk):
    return


def comments_delete(request, movie_pk, comments_pk):
    return


def likes(request, pk):
    return
