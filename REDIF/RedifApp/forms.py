from http import client
from django import forms

from RedifApp.models import Redacao, Filtro

class RedacaoForm(forms.ModelForm):
    class Meta:
        model = Redacao
        fields = ['titulo', 'area', 'tema', 'conteudo', 'descricao']
        

class FiltroForm(forms.ModelForm):
    class Meta:
        model = Filtro
        fields = "__all__"
        
