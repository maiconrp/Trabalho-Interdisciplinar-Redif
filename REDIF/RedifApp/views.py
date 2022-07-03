from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from matplotlib.style import context
from requests import request
from RedifApp.forms import RedacaoForm
from RedifApp.models import Redacao

from datetime import datetime

def home(request):
    return render(request,'home.html')


def listarRedacao(request):
    Redacoes = Redacao.objects.all()
    context = {
        "Redacao": Redacoes,
        'Logado': False,
        'Usuario' : False,
    }

    if User.is_authenticated:
        try:
            context['Usuario'] = request.user.id
            context['Logado'] = True
        except: pass

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
        nova_redacao = form.save(commit=False)

        nova_redacao.data_criacao = datetime.now()
        nova_redacao.fk_autor = User.objects.get(pk=user)
        nova_redacao.save()
        
        return redirect("/redif/listar")
        
    
    context = {
        'form' : form
    }

    return render(request, 'redacao/detalhar.html', context=context)


def detalharRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)

    context = {
        'Redacao' : redacao,
        'Autor' : redacao.fk_autor.username
    }

    return render(request, 'redacao/detalhar.html', context)


@login_required
def editarRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)

    if not redacao.fk_autor.id == request.user.id: 
        return redirect('/redif/listar')
    
    if request.method == "POST":
        form = RedacaoForm(request.POST, instance=redacao)
        if form.is_valid():
            form.save()
            return redirect("/redif/listar/")
    else:
        form = RedacaoForm(instance=redacao)

    context = {
        "form" : form,
        "id"   : id,
    }

    return render(request, "redacao/editar.html", context)


@login_required
def deletarRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    if redacao.fk_autor.id == request.user.id: 
        redacao.delete()
    return redirect('/redif/listar')

