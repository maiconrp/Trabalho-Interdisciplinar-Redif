from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("listar/", views.listarRedacao, name='listarRedacao'),
    path("", views.listarRedacao, name='listarRedacao'),
    path("home/", views.home, name='home'),
    path("criar/",  views.criarRedacao, name='criarRedacao'),
    path('detalhar/<int:id>/', views.detalharRedacao, name='detalharRedacao'),
    path('editar/<int:id>/', views.editarRedacao, name='editarRedacao'),
    path('deletar/<int:id>/', views.deletarRedacao, name='deletarRedacao'),
]