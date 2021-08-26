#Descricao: permitem que dados complexos, como querysets e instâncias de modelo,
#sejam convertidos em tipos de dados Python nativos que podem então são facilmente 
#renderizados em JSON, XML ou outros tipos de conteúdo.
#Aluno: Yan Silveira de Souza
#Data: 25/08/2021


from rest_framework import serializers
from alunos import models

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alunos
        fields = '__all__'