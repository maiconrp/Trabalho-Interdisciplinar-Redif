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
        max_length=20, 
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
        related_name="redacoesAvaliadas",
        through="Avaliacao"
    )

#conclui
class Avaliacao(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='Usuario_avaliacao'
    )
    redacao = models.ForeignKey(
        Redacao,
        on_delete=models.CASCADE,
        related_name='Usuario_avaliacao'
    )
    comentario = models.TextField(
        max_length=300, 
    )
    nota = models.SmallIntegerField(max_length=1000)

    data_criacao = models.DateTimeField(
        default=datetime.date.today
    )
    def __str__(self):
        return "Avaliador: {} - Redação Avaliada: {} - Nota dada: {}\n".format(self.usuario.username, self.redacao.titulo, self.nota)


class Filtro(models.Model):
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
        blank = True,
        null = True,
    )

    area = MultiSelectField(
        max_length=40, 
        max_choices=10,
        choices= AREA_CHOICES,
        blank = True,
        null = True,
        default=  ["CET", "CB", "CSA", "E", "LLA", "CH",]
    )

    tema = models.CharField(
        blank = True,
        null = True,
        max_length=45,
        default= 'All'
)




# class Comentario:

