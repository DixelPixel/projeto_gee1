from ast import Sub
from django.db import models


from .disciplina import *


# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length=200)
    disciplina = models.ManyToManyField(Disciplina)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
