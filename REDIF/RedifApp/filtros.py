
from RedifApp.models import Redacao

def filtrar(form):
    redacoes = Redacao.objects.all()

    if not form.is_valid(): return redacoes

    titulo = form.cleaned_data['titulo']
    area = form.cleaned_data['area']
    tema = form.cleaned_data['tema']

    if titulo: redacoes = redacoes.filter(titulo__icontains=  titulo) 
    if tema: redacoes = redacoes.filter(tema__icontains = tema) 

    if not area: return redacoes
    else: return filtrarArea(redacoes, area)


def filtrarArea(redacoes, areas):
    lista = []
    for item in list(redacoes):
        for x in list(item.area):
            if x in list(areas): 
                lista.append(item)
    return lista