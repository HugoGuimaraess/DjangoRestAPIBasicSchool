from django.shortcuts import render
from rest_framework import viewsets,generics
# Create your views here.
from escola.models import Aluno,Matricula,Curso
from escola.serializer import AlunoSerializer,MatriculaSerializer,CursoSerializer,ListaMatriculaAlunoSerializer,ListaAlunosMatriculadosCursoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ListaMatriculaAlunogenerics(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculaAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculadosCursoGenerics(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

