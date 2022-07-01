from datetime import date
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Redacao(models.Model):
    titulo = models.CharField(
        max_length = 45, 
        blank = False,
        null = False,
        default = 'Title',
    )

    area = models.CharField(
        blank=False, 
        null = False,
        max_length=45,
    )

    tema = models.CharField(
        blank=False, 
        null = False,
        max_length=45,
        default= 'topic'
    )

    data_criacao = models.DateTimeField(
        blank=False, 
        null = False,
        default= date.today,
    )

    conteudo = models.TextField(
        max_length=700,
        blank = False,
        null = False,
        
    )

    comentario = models.CharField(
        max_length=45, 
        blank= True,
        null= True,
        default=None
    )

    fk_autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
