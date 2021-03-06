from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_lista/', views.add_lista, name='add-lista'),
    path('listar_listas/', views.listar_listas, name='listar-listas'),
    path('visualizar_lista/<int:id>', views.visualizar_lista, name='visualizar-lista'),
    path('editar_lista/<int:id>', views.editar_lista, name='editar-lista'),
    path('deletar_lista/<int:id>', views.deletar_lista, name='deletar-lista'),
]