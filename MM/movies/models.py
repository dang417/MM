from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    user_id = models.ForeignKey(
        "accounts", on_delete=models.CASCADE)
