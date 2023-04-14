from django.db import models
from django.conf import settings

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, symmetrical=True, related_name='liked_movie')


class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
