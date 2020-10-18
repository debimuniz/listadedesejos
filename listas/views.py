from django.shortcuts import render
from .models import Lista
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


def listar_listas(request):
    listas = Lista.objects.all()
    return render(request, 'listas/listar_listas.html', context={'listas':listas})


def add_lista(request):
    if request.method == 'GET':
        return render(request, 'listas/add_lista.html')
    elif request.method == 'POST':
        nome = request.POST['nome']
        item1 = request.POST['item1']
        item2 = request.POST['item2']
        item3 = request.POST['item3']
        item4 = request.POST['item4']
        item5 = request.POST['item5']
        lista = Lista(nome=nome, item1=item1, item2=item2, item3=item3, item4=item4, item5=item5)
        lista.save()
        return HttpResponseRedirect('/listas/listar_listas')


def editar_lista(request, user_id):
    if request.method == 'GET':
        return render(request, 'listas/editar_lista.html', context={"user_id": user_id})
    elif request.method == 'POST':
        user_id = request.POST.get('user_id')
        nome = request.POST['nome']
        item1 = request.POST['item1']
        item2 = request.POST['item2']
        item3 = request.POST['item3']
        item4 = request.POST['item4']
        item5 = request.POST['item5']

        lista = Lista.objects.filter(id=user_id)
        lista.update = Lista(nome=nome, item1=item1, item2=item2, item3=item3, item4=item4, item5=item5)
        return HttpResponseRedirect('/listas/listar_listas')

def deletar_lista(request, user_id):
    if request.method == 'GET':
        lista = Lista.objects.filter(id=user_id)
        lista.delete()

    return HttpResponseRedirect('/listas/listar_listas')