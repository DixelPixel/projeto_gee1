from django.contrib import admin

from groups.models import *



# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title','date','location','curso',) 
    list_filter = ('location','date','curso','disciplina')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Group,GroupAdmin)
admin.site.register(Location)
admin.site.register(Student)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Messages)
admin.site.register(Eventos)