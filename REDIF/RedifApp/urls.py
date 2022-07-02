from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name = 'Tela inicial'),
    path("listar/", views.listRedactions, name='listRedactions'),
    path("create/",  views.create, name='create'),
    path('view/<int:id>/', views.view, name='read'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
