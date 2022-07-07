from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render

from RedifApp.forms import RedacaoForm, AvaliacaoForm

#importo a classe usuário
from RedifApp.models import Redacao, Usuario, Avaliacao

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

#-------------------------------------------------

def home(request):
    context = {
        'Usuario' : usuario(request),
    }
    return render(request, "home.html", context)

#-------------------------------------------------

def listarRedacao(request):
    Redacoes = Redacao.objects.all()
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
    
#-------------------------------------------------z

def detalharRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    autor = redacao.fk_autor.username

    context = {
        "TabelaAvaliacoes": Avaliacao,
        "Redacao" : redacao,
        "autor"   : autor,
        'Usuario' : usuario(request),
    }
    return render(request, "redacao/detalhar.html", context)
  
#-------------------------------------------------

@login_required
def editarRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    
    if request.method == "POST":
        form = RedacaoForm(request.POST, instance=redacao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/redif/")
    else:
        form = RedacaoForm(instance=redacao)

    context = {
        "url" : request.build_absolute_uri(),
        "Redacao" : redacao,
        "form" : form,
        "id"   : id,
        'Usuario' : usuario(request),
    }

    return render(request, "redacao/editar.html", context)

#-------------------------------------------------

@login_required
def deletarRedacao(request, id):
    Redacao.objects.get(pk=id).delete()
    return HttpResponseRedirect("/redif")

def addAvaliacao(request, id):

    # usuario = request.user.id
    if request.method == "POST":
        # form = AvaliacaoForm(request.POST, instance=redacao)
        comentario = request.POST.get("comentario")
        nota = request.POST.get("nota")
        print(comentario, nota)
        avaliacao = Redacao.objects.get(pk=id)
        try:
            print(avaliacao.Usuario_avalicao.first().usermame)
        except:pass
        avaliacao.avaliacoes.add(
            usuario(request), 
            through_defaults = {
                'comentario': comentario, 
                'nota' : nota
                }
            )      
        avaliacao.save()

        
        # (pk=usuario(request)).comentario       
        return HttpResponseRedirect("/redif/detalhar/"+str(id))
    else:
        form = AvaliacaoForm()

    

    return render(request, "redacao/detalhar.html")

