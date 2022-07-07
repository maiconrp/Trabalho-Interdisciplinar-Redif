import datetime
from tkinter import ALL
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Usuario
#adicionado la no settings.py

from multiselectfield import MultiSelectField
# Create your models here.   


class Redacao(models.Model):
    #area como um campo de multipla escolha
    AREA_CHOICES = (
        ("CET","Ciencias Exatas e da Terra"),
        ("CB","Ciências Biológicas"),
        ("CSA", "Ciências Sociais Aplicadas"),
        ("E","Engenharias"),
        ("LLA","Linguística, Letras e Artes"),        
        ("CH", "Ciências Humanas")
    )
    titulo = models.CharField(
        max_length = 45, 
        blank = False,
        null = False,
    )

    area = MultiSelectField(
        max_length=3, 
        max_choices=4,
        choices= AREA_CHOICES,
        blank=False, 
        null = False,
    )

    tema = models.CharField(
        blank=False, 
        null = False,
        max_length=45
    )
    #instancio a data de criação no momento em que o objeto é criado
    data_criacao = models.DateTimeField(
        default=datetime.date.today
    )

    conteudo = models.TextField(
        blank = False,
        null = False,
        max_length= 15000
    )
    
    #comentário
    descricao = models.TextField(
        max_length=300, 
        blank= True,
        null= True,
        default=None
    )

    #contagem simples de:
    curtidas = models.SmallIntegerField(default=0)
    compartilhamentos = models.SmallIntegerField(default=0)

    #Relaciono redação com a classe Usuario - 1 - N = " 1 Usuario escreve N redações"
    fk_autor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='Redacao'
    )
    #Relaciono redação com a classe Usuario - N - N = "N  Usuarios escrevem N redações" 
    avaliacoes = models.ManyToManyField(
        Usuario, 
        related_name="Avaliacoes",
        through="Avaliacoes"
    )

#conclui
class Avaliacoes(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='Usuario_avalicao'
    )
    redacao = models.ForeignKey(
        Redacao,
        on_delete=models.CASCADE,
        related_name='Redacao_avaliacao'
    )
    comentario = models.TextField(
        max_length=300, 
    )
    nota = models.SmallIntegerField()
    




# class Comentario:

