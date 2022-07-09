from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from matplotlib.style import context
from requests import request
from RedifApp.forms import RedacaoForm, FiltroForm
from RedifApp.models import Redacao

from datetime import datetime



def filtrar(form):
    redacoes = Redacao.objects.all()

    if not form.is_valid(): return redacoes

    titulo = form.cleaned_data['titulo']
    area = form.cleaned_data['area']
    tema = form.cleaned_data['tema']

    if titulo: redacoes = redacoes.filter(titulo__icontains=  titulo) 
    if tema: redacoes = redacoes.filter(tema__icontains = tema) 

    if not area: return redacoes

    lista = []
    for item in list(redacoes):
        for x in list(item.area):
            if x in list(area): 
                lista.append(item)
    return lista

#-------------------------------------------------

def home(request):
    context = {
        'Usuario' : usuario(request),
    }
    return render(request, "home.html", context)

#-------------------------------------------------

def listarRedacao(request):
    form = FiltroForm(request.POST)
    Redacoes = filtrar(form)

    context = {
        "Redacao": Redacoes,
        'Usuario' : usuario(request),
        'form' : form,
    }
    return render(request,"redacao/listar.html", context)



@login_required
def criarRedacao(request):

    if request.method == 'GET':
        form = RedacaoForm()
        context = {
            'form' : form,
            'Usuario' : usuario(request),
        }
        return render(request, 'redacao/criar.html', context=context)
    
    form = RedacaoForm(request.POST)
    user = request.user.id

    if form.is_valid():
        nova_redacao = form.save(commit=False)
        nova_redacao.data_criacao = datetime.now()
        nova_redacao.fk_autor = User.objects.get(pk=user)
        nova_redacao.save()
        return redirect("/redif/listar/")
        
    context = {
            'form' : form,
            'Usuario' : usuario(request),
    }

    return HttpResponse('404')


def detalharRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)

    context = {
        'Redacao' : redacao,
        'Usuario' : usuario(request),
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
        'Usuario' : usuario(request),
    }

    return render(request, "redacao/editar.html", context)


@login_required
def deletarRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    if redacao.fk_autor.id == request.user.id: 
        redacao.delete()
    return redirect('/redif/listar')


# Views relacionadas ao usuario

def usuario(request):
    Usuario = False
    
    if User.is_authenticated:
        try: 
            Usuario = request.user.id
            Usuario = Usuario.objects.get(pk=Usuario)
        except: pass
    
    return Usuario


def perfilUsuario(request, usuario):
    perfil = User.objects.get(pk = request.user.id)
    Redacoes = Redacao.objects.filter(fk_autor= perfil)
    context = {
        'Redacao': list(Redacoes),
    }
    
    return render(request,'redacao/redacoes-usuario.html', context)

