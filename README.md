# apirestdb
 API REST com Django
# Introdução
A ideia do projeto é que possamos armazenar alunos e seus atributos dentro de um banco de dados e realizar as operações de CRUD sem precisar de uma interface gráfica. Assim, outra aplicação poderá se comunicar com a nossa de forma eficiente.<br> Esse é o conceito de API (Application Programming Interface)

# Preparando o ambiente

```bash
>python -m venv venv #criando ambiente virtual na sua versao do python
>./venv/Scripts/Activate #Ativando o ambiente virtual
>pip install django djangorestframework #instalação local das nossas dependências
```
O lance do ambiente virtual é que todas suas dependências *(que no python costumam ser muitas)*  ficam apenas num diretório específico. <br>
Logo, com uma venv você pode criar projetos que usam versões diferentes da mesma biblioteca sem que haja conflito na hora do import.

# Projeto x App
No django cada **project** pode carregar múltiplos **apps**, como um projeto site de esportes que pode ter um app para os artigos, outro para rankings etc.<br>
Ainda no terminal usamos os comandos a seguir para criar o project **library** que vai carregar nosso app **books**. 

```bash
>django-admin startproject apirestdb . #ponto indica diretório atual
>django-admin startapp alunos
>python manage.py runserver #pra levantarmos o servidor local com a aplicação
```

Para criar as tabelas no banco de dados (Por enquanto *Sqlite3*) executamos o comando
```bash
>python manage.py migrate
```
Isso evita que a notificação *unapplied migrations* apareça na próxima vez que você levantar o servidor 

# Criando os modelos e API
No arquivo **./library/settings.py** precisamos indicar ao nosso projeto library sobre a existência do app books e também o uso do rest framework. Portanto adicionamos as seguintes linhas sublinhadas

Já que nossa API suporta imagens como atributos também sera necessário o seguite acrescimo de codigo em **./library/settings.py**
```py
MEDIA_URL = '/media'
 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Agora em **./library/books/models.py** iremos criar nosso modelo com os atributos que um livro deve ter.

```py
from django.db import models
from uuid import uuid4


class Alunos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    ano_de_matricula = models.IntegerField()
```
## Serializers e Viewsets
Dentro de **./library/alunos** iremos criar a pasta **/api** com os arquivos 
* serializers.py 
* viewsets.py 

### Serializers
```py
from rest_framework import serializers
from alunos import models

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alunos
        fields = '__all__' #todos os campos do model id, name..
```

### Viewsets
```py
from rest_framework import viewsets
from alunos.api import serializers
from alunos import models

class AlunosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlunosSerializer
    queryset = models.Alunos.objects.all() #tambem todos os campos do nosso modelo
```
# Criação das rotas
Agora com o viewset e o serializer a única coisa que falta é uma rota. Portanto vamos para **./library/urls.py** resolver esse problema

```py
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from books.api import viewsets as booksviewsets
#criando nosso objeto de rota
route = routers.DefaultRouter()
route.register(r'books', booksviewsets.BooksViewSet, basename="Books")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Como criamos um modelo novo lá em cima, precisamos avisar e em seguida migrar todos essas novas informações para o banco de dados

```bash
>python manage.py makemigrations 
>python manage.py migrate
>python manage.py runserver 
```
Agora você pode usar um programa como <a href="https://insomnia.rest/">Insomnia</a> para testar os métodos http no link do seu servidor local.

>O python facilita bastante coisas para a gente, como os serializers (que convertem objetos para strings na comunicação cliente-servidor) e os verbos http (GET, POST, PUT, DELETE) que de certa forma também vem por padrão. Não me aprofundei neles durante o readme porque também preciso entender melhor como essas coisas funcionam

# Getting Started
```bash
# Clone repository
git clone https://github.com/yansilveira00/apirestdb.git

# Create Virtual Environment
python -m venv venv && ./venv/Scripts/Activate

# Install dependencies
pip install django djangorestframework

# Run Application
python manage.py runserver
```
