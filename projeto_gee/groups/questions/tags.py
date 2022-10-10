from ast import Sub
from django.db import models

from ..model.student import *



class Tag(models.Model):
    name = models.CharField(max_length=200)
    student = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name
