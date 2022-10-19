from django.contrib import admin
from .model.groups import Group
from .model.messages import Messages
from .model.eventos import Eventos
from .model.location import Location
from .model.student import Student
from .model.curso import Curso
from .model.disciplina import Disciplina
from .questions.questions import Question
from .questions.study_method import Study_method
from .questions.tags import Tag
from .questions.answer import Answer


# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'curso',)
    list_filter = ('location', 'date', 'curso', 'disciplina')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Group, GroupAdmin)
admin.site.register(Location)
admin.site.register(Student)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Messages)
admin.site.register(Eventos)
admin.site.register(Question)
admin.site.register(Study_method)
admin.site.register(Tag)
admin.site.register(Answer)
