from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns  =  [
    path("home",                views.home,             name = 'Tela inicial'),
    path("criar/",              views.criarRedacao,     name = 'criarRedacao'),
    path("",                    views.listarRedacao,    name = 'listarRedacao'),
    path('editar/<int:id>/',    views.editarRedacao,    name = 'editarRedacao'),
    path('detalhar/<int:id>/',  views.detalharRedacao,  name = 'detalharRedacao'),
    path('deletar/<int:id>/',   views.deletarRedacao,   name = 'deletarRedacao'),
]
