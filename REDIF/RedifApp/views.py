from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from RedifApp.forms import RedacaoForm
from RedifApp.models import Redacao

from datetime import datetime

def PaginaInicial(request):
    return render(request, 'home.html')

def ListarRedacoes(request):
    redacoes = Redacao.objects.all()
    context = {
        "Redacoes": redacoes,
    }
    return render(request, 'redacao/listar.html', context)

@login_required
def CriarRedacao(request):
    if request.method == 'GET':
        form = RedacaoForm()
        context = {
            'form': form
        }
        return render(request, 'redacao/criar.html', context)

    form = RedacaoForm(request.POST)
    user = request.user.id
    user = User.objects.get(pk=user)
    print(type(user))
    if form.is_valid():
        title       = form.cleaned_data['title']
        area        = form.cleaned_data['area' ]
        topic       = form.cleaned_data['topic']
        content     = form.cleaned_data['title']
        comment     = form.cleaned_data['title']
        dateCreation = datetime.now()
        fk_autor    = user
        new_redacao = Redacao(title=title, area=area, topic=topic, content=content,
                              comment=comment, dateCreation=dateCreation, fk_autor=fk_autor)
        new_redacao.save()
    context = {
        'form': form
    }
    return render(request, 'redacao/listar.html', context)

def view(request, id):
    data = {}
    redacao = Redacao.objects.get(pk=id)
    print(redacao)
    autor = redacao.fk_autor.username
    data = {
        'Redacao': redacao,
        'autor': autor
    }
    return render(request, 'redacao/detail.html', data)


def edit(request, id):
    pass


@login_required
def delete(request, id):
    pass
