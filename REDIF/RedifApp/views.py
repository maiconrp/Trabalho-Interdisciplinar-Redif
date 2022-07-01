from django.shortcuts import render

# Create your views here.
import re
from django.shortcuts import redirect, render
from matplotlib.style import context
from requests import request
from RedifApp.forms import RedacaoForm
from RedifApp.models import Redacao


def create(request):
    if request.method == 'GET':
        form = RedacaoForm()
        context = {
        'form' : form
        }
        return render(request, 'cadastro/cadastro.html', context=context)
    else:
        form = RedacaoForm(request.POST)
        if form.is_valid():
            Redacao = form.save()
            form = RedacaoForm()
        
        context = {
            'form' : form
        }
    return render(request, 'cadastro/cadastro.html', context=context)


def view(request, pk):
    data = {}
    data['Redacao'] = Redacao.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['Redacao'] = Redacao.objects.get(pk=pk)
    data['form'] = RedacaoForm(instance=data['Redacao'])
    return render(request, 'cadastro/cadastro.html')

def update(request, pk):
    data = {}
    data['Redacao'] = Redacao.objects.get(pk=pk)
    form = RedacaoForm(request.POST or None, instance=data['Redacao'])
    if form.is_valid():
        form.save()
        return redirect('Redacaos')
