#Descricao: permite combinar a lógica de um conjunto de visualizações relacionadas 
#em uma única classe, chamada ViewSet.
#Aluno: Yan Silveira de Souza
#Data: 25/08/2021

from rest_framework import viewsets
from alunos.api import serializers
from alunos import models

class AlunosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlunosSerializer
    queryset = models.Alunos.objects.all()