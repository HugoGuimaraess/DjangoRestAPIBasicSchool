from django.db import models
from datetime import datetime
# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    rg = models.CharField(max_length=9,null=False,blank=False)
    cpf=models.CharField(max_length=11,null=False,blank=False)
    nascimento= models.DateTimeField(default=datetime.now,null=False)
    celular = models.CharField(max_length=11,default='')

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = [
        ('A','Básico'),
        ('B','Intermediário'),
        ('C','Avançado')
    ]

    cod_curso = models.CharField(max_length=10)
    descricao = models.TextField(null=False,blank=False)
    nivel = models.CharField(max_length=1,choices=NIVEL,default='A',null=False,blank=False)

    def __str__(self):
        return self.descricao



class Matricula(models.Model):
    PERIODO = [
        ('M','Matutino'),
        ('V','Verspertino'),
        ('N','Noturno')
    ]


    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    periodo = models.CharField(choices=PERIODO,max_length=1,blank=False,null=False,default='M')
