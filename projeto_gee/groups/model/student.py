from ast import Sub
from django.db import models


class Student(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
