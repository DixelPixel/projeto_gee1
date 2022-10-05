from django.db import models

from .location import Location
from .student import Student
from .curso import Curso
from .disciplina import Disciplina


# Create your models here.


class Group(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.slug}'
