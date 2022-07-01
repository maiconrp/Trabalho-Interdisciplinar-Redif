from datetime import date
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Redacao(models.Model):
    title = models.CharField(
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

    topic = models.CharField(
        blank=False, 
        null = False,
        max_length=45,
        default= 'topic'
    )

    dateCreation = models.DateTimeField(
        blank=False, 
        null = False,
        default= date.today,
    )

    content = models.TextField(
        max_length=700,
        blank = False,
        null = False,
    )

    comment = models.CharField(
        max_length=45, 
        blank= True,
        null= True,
        default=None
    )

    fk_autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
