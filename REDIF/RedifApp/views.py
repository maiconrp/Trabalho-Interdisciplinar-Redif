from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render


from RedifApp.forms import RedacaoForm

#importo a classe usuário
from RedifApp.models import Redacao, Usuario

# remover
# from django.contrib.auth.models import User
# from datetime import datetime

#ainda falta mesclar com algumas alterações da views da master

#O que antes era classe "User", passa a ser "Usuario"

#melhor coisa essa funçãokkkkkkkk salvou
def usuario(request):
    user = False
    if Usuario.is_authenticated:
        try: 
            user = request.user.id
            user = Usuario.objects.get(pk=user)
        except: 
            pass
    return user



def filtrar(request):
    titulo = request.GET.get('titulo')
    area = request.GET.get('area')
    tema = request.GET.get('tema')
    autor = request.GET.get('autor')

    redacoes = Redacao.objects.all()

    if titulo: redacoes.filter(titulo__icontains = titulo) 
    if area: redacoes.filter(area__icontains = area) 
    if tema: redacoes.filter(tema__icontains = tema) 
    if autor: redacoes.filter(autor__icontains = autor) 

    return redacoes

#-------------------------------------------------

def home(request):
    context = {
        'Usuario' : usuario(request),
    }
    return render(request, "home.html", context)

#-------------------------------------------------

def listarRedacao(request):
    Redacoes = Redacao.objects.all()
    if request.GET:
        print('oi')
        
    context = {
        "Redacao": Redacoes,
        'Usuario' : usuario(request),
        }
    return render(request,"redacao/listar.html", context)

#-------------------------------------------------

@login_required
def criarRedacao(request):
    
    if request.method == 'POST':
        form = RedacaoForm(request.POST)
        if form.is_valid():
            nova_redacao = form.save(commit=False)
            nova_redacao.fk_autor = usuario(request)
            nova_redacao.save()
            context = {'form' : form,'Usuario' : usuario(request)}
            return HttpResponseRedirect("/redif")
    else:
        form = RedacaoForm()

    context = {
        'form' : form,
        'Usuario' : usuario(request),
    }
    return render(request, 'redacao/criar.html', context)
    
#-------------------------------------------------

def detalharRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    autor = redacao.fk_autor.username

    context = {
        "Redacao" : redacao,
        "autor"   : autor
    }
    return render(request, "redacao/detalhar.html", context)
  
#-------------------------------------------------

@login_required
def editarRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    
    if not usuario(request) == redacao.fk_autor:
        print('Acesso negado')

    if request.method == "POST":
        form = RedacaoForm(request.POST, instance=redacao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/redif/")
    else:
        form = RedacaoForm(instance=redacao)

    context = {
        "form" : form,
        "id"   : id,
    }

    return render(request, "redacao/editar.html", context)

#-------------------------------------------------

@login_required
def deletarRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    if usuario(request) == redacao.fk_autor:
        redacao.delete()
    return HttpResponseRedirect("/redif")
