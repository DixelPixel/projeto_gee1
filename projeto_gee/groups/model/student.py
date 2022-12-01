from ast import Sub
from django.db import models


class Student(models.Model):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    senha = models.CharField(max_length=20)
    confirmar = models.CharField(max_length=20)

    def __str__(self):
        return self.email
