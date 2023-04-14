from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    user_id = models.ForeignKey("accounts", on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie_id = models.ForeignKey("Movie", on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
