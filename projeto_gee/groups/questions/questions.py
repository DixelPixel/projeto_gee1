from ast import Sub
from django.db import models

from ..model.student import Student



class Question(models.Model):
    name = models.CharField(max_length=200)
    statement = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.name
