from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'movies/index.html')


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
