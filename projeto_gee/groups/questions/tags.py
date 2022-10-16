from ast import Sub
from django.db import models

from ..model.student import Student
from .questions import Question
from .study_method import Study_method


class Tag(models.Model):
    name = models.CharField(max_length=200)
    student = models.ManyToManyField(Student, blank=True, null=True)
    question = models.ManyToManyField(Question, blank=True, null=True)
    study_method = models.ManyToManyField(Study_method, blank=True, null=True)

    def __str__(self):
        return self.name
