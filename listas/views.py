from django.shortcuts import render
from .models import Lista
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.core import serializers


def listar_listas(request):
    #my_user = Usuario.objects.get(login=request.session['username'])
    listas = Lista.objects.all()
    return render(request, 'listas/listar_listas.html', context={'listas':listas})

#
# View para visualizar uma lista em particular
#
def visualizar_lista(request, id):
    lista = Lista.objects.get(id=id)
    return render(request, template_name='listas/visualizar_lista.html', context={'lista': lista})


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


def editar_lista(request, id):
    if request.method == 'GET':
        lista = Lista.objects.get(id=id)
        return render(request, 'listas/editar_lista.html', context={"lista": lista})
    elif request.method == 'POST':
        id = request.POST.get('id')
        nome  = request.POST['nome']
        item1 = request.POST['item1']
        item2 = request.POST['item2']
        item3 = request.POST['item3']
        item4 = request.POST['item4']
        item5 = request.POST['item5']

        lista = Lista.objects.get(id=id)
        lista.nome = nome
        lista.item1 = item1
        lista.item2 = item2
        lista.item3 = item3
        lista.item4 = item4
        lista.item5 = item5
        Lista.save(lista)
        return HttpResponseRedirect('/listas/listar_listas')

def deletar_lista(request, id):
    if request.method == 'GET':
        lista = Lista.objects.get(id=id)
        lista.delete()

    return HttpResponseRedirect('/listas/listar_listas')