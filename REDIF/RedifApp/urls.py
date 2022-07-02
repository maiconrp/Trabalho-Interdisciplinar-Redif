from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns  =  [
    path("home",                views.home,             name = 'Tela inicial'),
    path("criar/",              views.CriarRedacao,     name = 'criarRedacao'),
    path("",                    views.ListarRedacao,    name = 'listarRedacao'),
    path('editar/<int:id>/',    views.EditarRedacao,    name = 'editarRedacao'),
    path('detalhar/<int:id>/',  views.DetalharRedacao,  name = 'detalharRedacao'),
    path('deletar/<int:id>/',   views.DeletarRedacao,   name = 'deletarRedacao'),
]
