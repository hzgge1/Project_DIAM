from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Utilizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imageURL = models.CharField(max_length=100, default="")
    descricao = models.CharField(max_length=500,default="")
    numeroQuestoes = models.IntegerField(default=0)

# Create your models here.
class Questao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questao_titulo = models.CharField(max_length=100, default="")
    questao_descricao = models.CharField(max_length=500, default="")
    questao_data = models.DateTimeField('data da publicacao')
    tags = models.ManyToManyField('Tag', related_name='questao')
    numero_likes = models.IntegerField(default=0)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    questao = models.ForeignKey(Questao, on_delete=models.SET_NULL, null=True)
class Resposta(models.Model):
    # se eliminar a questao elimina as respostas
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resposta_texto = models.CharField(max_length=10000)
    resposta_data = models.DateTimeField('data da resposta')


class Tag(models.Model):
    tag_texto = models.CharField(max_length=30)