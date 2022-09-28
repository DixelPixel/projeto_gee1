#from msvcrt import open_osfhandle
from ast import Sub
from django.db import models




class Student(models.Model):
    email = models.EmailField(unique= True)

    
    def __str__(self):
        return self.email

# Create your models here.
class Disciplina (models.Model):
    code = models.CharField(max_length=200)
    student = models.ManyToManyField(Student)
    

    def __str__(self):
        return self.code

class Curso(models.Model):
    name = models.CharField(max_length=200)
    disciplina = models.ManyToManyField(Disciplina)
    student = models.ManyToManyField(Student)


    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'



class Group(models.Model):
    title = models.CharField(max_length = 200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    #image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    student = models.ManyToManyField(Student)
    curso = models.ForeignKey(Curso,on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina,on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.title}-{self.slug}'

class Eventos(models.Model):
    name = models.CharField(max_length = 200)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.name} {self.location}'


class Messages(models.Model):
    poster = models.CharField(max_length = 200)
    description = models.CharField(max_length =200)
    group = models.ForeignKey(Group,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.poster} ({self.description})'

    