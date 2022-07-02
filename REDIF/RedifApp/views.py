from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from matplotlib.style import context
from requests import request
from RedifApp.forms import RedacaoForm
from RedifApp.models import Redacao

from datetime import datetime

def listarRedacao(request):
    Redacoes = Redacao.objects.all()
    context = {"Redacao": Redacoes}

    return render(request,'redacao/listar.html', context)

@login_required
def criarRedacao(request):

    if request.method == 'GET':
        form = RedacaoForm()
        context = {
        'form' : form
        }
        return render(request, 'redacao/criar.html', context=context)
    
    form = RedacaoForm(request.POST)
    user = request.user.id

    if form.is_valid():
        titulo = form.cleaned_data['titulo']
        area = form.cleaned_data['area']
        tema = form.cleaned_data['tema']
        conteudo = form.cleaned_data['conteudo']
        comentario = form.cleaned_data['comentario']
        data_criacao = datetime.now()
        fk_autor = User.objects.get(pk=user)

        nova_redacao = Redacao(
            titulo= titulo, 
            area= area, 
            tema= tema, 
            conteudo= conteudo, 
            comentario= comentario, 
            data_criacao= data_criacao, 
            fk_autor= fk_autor,
        )
        nova_redacao.save()
        
    
    context = {
        'form' : form
    }

    return render(request, 'redacao/detalhar.html', context=context)


def detalharRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    autor = redacao.fk_autor.username
    context = {
        'Redacao' : redacao,
        'autor' : autor
    }

    return render(request, 'redacao/detalhar.html', context)

@login_required
def editarRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)

    if request.method == 'POST':
        form = RedacaoForm(request.POST, instance=redacao)

        if form.is_valid():
            form.save()
            return redirect('/redif/listar')
    
    form = RedacaoForm(instance=redacao)
    context = {
        'form' : form,
        'id' : id,
    }

    return render(request, 'redacao/editar.html', context=context)



@login_required
def deletarRedacao(request, id):
    Redacao.objects.get(pk=id).delete()
    return redirect('/redif/listar')

