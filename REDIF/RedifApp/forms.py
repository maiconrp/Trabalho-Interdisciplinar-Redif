from django import forms
from RedifApp.models import Redacao, Avaliacao

class RedacaoForm(forms.ModelForm):
    class Meta:
        model = Redacao
        fields = ['titulo', 'area', 'tema', 'conteudo', 'descricao']

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['comentario', 'nota']
        
