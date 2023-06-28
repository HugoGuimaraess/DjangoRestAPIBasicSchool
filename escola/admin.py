from django.contrib import admin
from escola.models import Curso,Matricula,Aluno
# Register your models here.



class ListaAluno(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 10


admin.site.register(Aluno,ListaAluno)


class ListaCurso(admin.ModelAdmin):
    list_display = ('id','cod_curso','descricao')
    list_display_links = ('id','cod_curso')
    search_fields = ('cod_curso',)


admin.site.register(Curso,ListaCurso)



class ListaMatricula(admin.ModelAdmin):
    list_display = ('id','aluno','curso','periodo')
    list_display_links = ('id',)


admin.site.register(Matricula,ListaMatricula)