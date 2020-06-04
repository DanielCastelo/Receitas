from django.db import models
from datetime import datetime #pega a data atual

class Receita(models.Model): #criação da classe "receita", que é uma subclasse de (models.Model)
    nome_receita = models.CharField(max_length=200) #CharField é um campo para digitar strings (nesse caso com limite de 200 caracteres)
    ingredientes = models.TextField() #TextField abre uma caixa para dgitar um texto
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField() #IntegerField trabalha com números inteiros
    rendimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True) #registra a hora que a receita foi publicada (blank=true premite que o campo fique em branco)

# o comando "python manage.py makemigrations" cria uma lista de dados para migração ao banco postgre
# o arquivo 0001_initial contém os dados desta lista
# o comando "python manage.py migrate" é quem de fato vai enviar tudo para o banco

#o proprio django já se encarrega de criar um campo "id" como chave primária, dentro do postgree, então não é necessario criar isso aqui. 