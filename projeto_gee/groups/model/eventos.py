from ast import Sub
from django.db import models
from .location import Location
from .student import Student


class Eventos(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.name} {self.location}'
