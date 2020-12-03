from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_usuarios, name='listar-usuarios'),
    path('add_usuario/', views.add_usuario, name='add-usuario'),
    path('editar_usuario/<int:user_id>', views.editar_usuario, name='editar-usuario'),
    path('deletar_usuario/<int:user_id>', views.deletar_usuario, name='deletar-usuario'),
    path('home_usuario/', views.home_usuario, name='home_usuario')
]