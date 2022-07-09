from django.db import models
from django.contrib.auth.models import User

# Create your models here.   

#Crio classe Usuário e faço herdar de User, restando apenas adcionar os campos especificos
class Usuario(User):
    
    TITULACAO_CHOICES = (
        ("1", "Fundamental 2 ao 8°ano"),
        ("2", "Cursando 9° ano"),
        ("3", "Cursando Ensino Médio"),
        ("4", "Ensino Médio Completo"),
        ("5", "Ensino Médio Incompleto"),
        ("6", "Cursando Ensino Superior"),        
        ("7", "Ensino Superior Completo")
    )

    CONDICAO_CHOICES = {
        ("P", "Professor"),
        ("A", "Aluno")
    }

    #verifica a titulacao do usuario
    titulacao = models.CharField(
        max_length=1, 
        choices= TITULACAO_CHOICES,
        blank=False, 
        null = False,
    )
    #verifica se é aluno ou professor
    condicao = models.CharField(
        max_length=1, 
        choices= CONDICAO_CHOICES,
        blank=False, 
        null = False,
    )

