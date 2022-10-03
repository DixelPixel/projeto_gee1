from ast import Sub
from django.db import models
from .groups import Group


class Messages(models.Model):
    poster = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.poster} ({self.description})'
