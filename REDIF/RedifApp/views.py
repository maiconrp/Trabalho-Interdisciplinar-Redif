from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.models import User

from RedifApp.forms import RedacaoForm, AvaliacaoForm, FiltroForm
from RedifApp.models import Redacao
from accounts.models import Usuario
from . import filtros

titulacao = {
        "1" : "Fundamental 2 ao 8°ano",
        "2" : "Cursando 9° ano",
        "3" : "Cursando Ensino Médio",
        "4" : "Ensino Médio Completo",
        "5" : "Ensino Médio Incompleto",
        "6" : "Cursando Ensino Superior",        
        "7" : "Ensino Superior Completo",
    }

condicao = {
        "P": "Professor",
        "A": "Aluno"
    }



def perfilUsuario(request, user):

    perfil = Usuario.objects.filter(username = user)
    Redacoes = Redacao.objects.filter(fk_autor= perfil[0])
   
    context = {
        'Redacao': list(Redacoes),
        'Perfil' : perfil[0],
        'Usuario' :  usuario(request),
        'Titulacao' : str(titulacao[perfil[0].titulacao]),
        'Condicao' : str(condicao[perfil[0].condicao]),
        'Username' : str(perfil[0].username).upper()
    }
    
    return render(request,'redacao/perfil-usuario.html', context)

def usuario(request):
    user = False
    if Usuario.is_authenticated:
        try: 
            user = request.user.id
            user = Usuario.objects.get(pk=user)
        except: pass
    return user

#-------------------------------------------------

def home(request):
    context = {
        'Usuario' : usuario(request),
    }
    return render(request, "home.html", context)

#-------------------------------------------------

def PagDicas(request, iDica):
    Redacoes = Redacao.objects.all() 
    Dicas = {
        'PagDicasGeral' : 'PagDicasGeral', #Pag-Dicas/PagDicasGeral
        'Introducao'    : 'introducao',#Pag-Dicas/Introducao
        'Passo-a-passo' : 'passo-a-passo',#Pag-Dicas/Passo-a-passo
        'ComoF'         : 'ComoF',#Pag-Dicas/ComoF
        'conclusao'     : 'conclusao',#Pag-Dicas/conclusao
        'desenvolvimento': 'desenvolvimento'#Pag-Dicas/desenvolvimento
    }
    if iDica in Dicas.keys():
        return render(request, 'PaginaDeDicas/' + Dicas[iDica] + '.html', {'Redacoes' : Redacoes })
    else: 
        return render(request, 'PaginaDeDicas/PagDicasGeral.html', {'Redacoes' : Redacoes })

#-------------------------------------------------

def listarRedacao(request):
    form = FiltroForm(request.POST)
    Redacoes = filtros.filtrar(form)

    context = {
        "Redacao": Redacoes,
        'Usuario' : usuario(request),
        'form' : form,
    }
    return render(request,"redacao/listar.html", context)

@login_required
def criarRedacao(request):
    
    if request.method == 'POST':
        form = RedacaoForm(request.POST)

        if form.is_valid():
            nova_redacao = form.save(commit=False)
            nova_redacao.fk_autor = usuario(request)
            nova_redacao.save()

            context = {
                'form'    : form,
                'Usuario' : usuario(request)
            }
            return HttpResponseRedirect("/redif")
    
    else:form = RedacaoForm()

    context = {
        'form'    : form,
        'Usuario' : usuario(request),
    }
    
    return render(request, 'redacao/criar.html', context)
    
#-------------------------------------------------

def detalharRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    autor = redacao.fk_autor.username

    context = {
        "url"     : request.build_absolute_uri(),
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
        "Redacao" : redacao,
        "form"    : form,
        "id"      : id,
        'Usuario' : usuario(request),
    }

    return render(request, "redacao/editar.html", context)

#-------------------------------------------------

@login_required
def deletarRedacao(request, id):
    Redacao.objects.get(pk=id).delete()
    return HttpResponseRedirect("/redif")

#-------------------------------------------------

@login_required
def addAvaliacao(request, id):
   
    if request.method == "POST":
        
        comentario = request.POST.get("comentario")
        nota = request.POST.get("nota")

        avaliacao = Redacao.objects.get(pk=id)
        
        avaliacao.avaliacoes.add(
            usuario(request), 
            through_defaults = {
                'comentario': comentario, 
                'nota' : nota
                }
            )
                  
        avaliacao.save()
      
        return HttpResponseRedirect("/redif/detalhar/"+str(id))

    else:
        form = AvaliacaoForm() 

    return render(request, "redacao/detalhar.html")

