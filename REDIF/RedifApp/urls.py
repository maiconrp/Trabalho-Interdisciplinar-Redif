from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns  =  [
    path("Pag-Dicas/<str:iDica>",           views.PagDicas,         name = 'PagDicas'),
    path("home/",                           views.home,             name = 'Tela inicial'),
    path("criar/",                          views.criarRedacao,     name = 'criarRedacao'),
    path("perfil/<str:user>/",              views.perfilUsuario,    name = 'perfilUsuario'),

    path("",                                views.listarRedacao,    name = 'listarRedacao'),
    path("listar/",                         views.listarRedacao,    name = 'listarRedacao'),
    path('editar/<int:id>/',                views.editarRedacao,    name = 'editarRedacao'),
    path('detalhar/<int:id>/',              views.detalharRedacao,  name = 'detalharRedacao'),
    path('deletar/<int:id>/',               views.deletarRedacao,   name = 'deletarRedacao'),
    path('detalhar/comentar/<int:id>/',     views.addAvaliacao,     name = 'addAvaliacao'),
    
]
