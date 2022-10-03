#from msvcrt import open_osfhandle
from ast import Sub
from django.db import models

from .student import Student

# Create your models here.


class Disciplina (models.Model):
    code = models.CharField(max_length=200)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.code
