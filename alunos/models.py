#Descricao: criando atributos para os alunos
#Aluno: Yan Silveira de Souza
#Data: 25/08/2021

from django.db import models
from uuid import uuid4

class Alunos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    ano_de_matricula = models.IntegerField()