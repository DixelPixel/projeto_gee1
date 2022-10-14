from ast import Sub
from django.db import models

from ..model.student import *
from .questions import Question
from .study_method import Study_method


class Tag(models.Model):
    name = models.CharField(max_length=200)

    student = models.ForeignKey(Student, blank=True,on_delete=models.CASCADE)
    question = models.ManyToManyField(Question, blank=True)
    study_method = models.ManyToManyField(Study_method, blank=True)

    def __str__(self):
        return self.name
