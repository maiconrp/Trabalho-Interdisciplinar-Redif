from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render

from django.contrib.auth.models import User
from RedifApp.forms import RedacaoForm
from RedifApp.models import Redacao

from datetime import datetime

def home(request):
    return render(request, "home.html")

def listarRedacao(request):
    Redacoes = Redacao.objects.all()

    context = {
        "Redacao": Redacoes
        }

    if User.is_authenticated:
        try:
            Usuario = request.user.id
            context ["Usuario"] = User.objects.get(pk=Usuario)
            context ["Logado"]  = True

        except: pass

    return render(request,"redacao/listar.html", context)

@login_required
def criarRedacao(request):
    user = request.user.id
    form = RedacaoForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            nova_redacao = form.save(commit=False)

            nova_redacao.data_criacao = datetime.now()
            nova_redacao.fk_autor = User.objects.get(pk=user)

            nova_redacao.save()
            return HttpResponseRedirect("/redif")
        else:
            form = RedacaoForm()

    context = {
        "form": form
    }

    return render(request, "redacao/criar.html", context)

def detalharRedacao(request, id):
    redacao = Redacao.objects.get(pk=id)
    autor = redacao.fk_autor.username

    context = {
        "Redacao" : redacao,
        "autor"   : autor
    }
    return render(request, "redacao/detalhar.html", context)

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
        "form" : form,
        "id"   : id,
    }

    return render(request, "redacao/editar.html", context)

@login_required
def deletarRedacao(request, id):
    Redacao.objects.get(pk=id).delete()
    return HttpResponseRedirect("/redif")
