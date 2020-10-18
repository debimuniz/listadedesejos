from django.shortcuts import render
from .models import Usuario
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', context={'usuarios':usuarios})


def add_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuarios/add_usuario.html')
    elif request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        data_aniversario = request.POST.get('data_aniversario')
        login = request.POST['login']
        senha = request.POST['senha']
        email = request.POST['email']
        usuario = Usuario(nome=nome, sobrenome=sobrenome, data_aniversario=data_aniversario, login=login, senha=senha, email=email)
        usuario.save()
        return HttpResponseRedirect('/listas/add_lista')


def editar_usuario(request, user_id):
    if request.method == 'GET':
        return render(request, 'usuarios/editar_usuario.html', context={"user_id": user_id})
    elif request.method == 'POST':
        user_id = request.POST.get('user_id')
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        login = request.POST['login']
        senha = request.POST['senha']
        email = request.POST['email']

        usuario = Usuario.objects.filter(id=user_id)
        usuario.update(nome=nome, sobrenome=sobrenome, login=login, senha=senha, email=email)
        return HttpResponseRedirect('/usuarios/listar')


def deletar_usuario(request, user_id):
    if request.method == 'GET':
        usuario = Usuario.objects.filter(id=user_id)
        usuario.delete()

    return HttpResponseRedirect('/usuarios/listar')