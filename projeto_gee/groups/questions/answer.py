from ast import Sub
from django.db import models
from .questions import Question
from ..const import AGREE_LEVELS


class Answer(models.Model):
    answer = models.CharField(
        max_length=10
    )

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
