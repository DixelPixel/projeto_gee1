from ast import Sub
from django.db import models

from ..model.student import Student
from .tags import Tag


class Question(models.Model):
    name = models.CharField(max_length=200)
    statement = models.CharField(max_length=2000)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
