from ast import Sub
from django.db import models




class Study_method(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
