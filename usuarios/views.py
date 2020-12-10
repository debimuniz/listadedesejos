from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Usuario
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from listas.models import Lista


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', context={'usuarios': usuarios})


#
# Adding a User
#
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
        if request.FILES:
            foto = request.FILES['foto']
            usuario = Usuario(nome=nome, sobrenome=sobrenome, data_aniversario=data_aniversario, login=login,
                              senha=senha, email=email, foto=foto)
        else:
            usuario = Usuario(nome=nome, sobrenome=sobrenome, data_aniversario=data_aniversario, login=login,
                              senha=senha, email=email)
        usuario.save()
        return HttpResponseRedirect('/login')


def editar_usuario(request, user_id):
    if request.method == 'GET':
        return render(request, 'usuarios/editar_usuario.html', context={"user_id": user_id})
    elif request.method == 'POST':
        user_id = request.POST.get('user_id')
        usuario = Usuario.objects.filter(id=user_id)

        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        data_aniversario = request.POST['data_aniversario']
        login = request.POST['login']
        senha = request.POST['senha']
        email = request.POST['email']
        if request.FILES:
            foto = request.FILES['foto']
            usuario.update(nome=nome, sobrenome=sobrenome, data_aniversario=data_aniversario, login=login,
                              senha=senha, email=email, foto=foto)
        else:
            usuario.update(nome=nome, sobrenome=sobrenome, data_aniversario=data_aniversario, login=login,
                              senha=senha, email=email)
        return HttpResponseRedirect('/usuarios/listar')


def deletar_usuario(request, user_id):
    if request.method == 'GET':
        usuario = Usuario.objects.filter(id=user_id)
        usuario.delete()

    return HttpResponseRedirect('/usuarios/listar')


def home_usuario(request):
    usuario = Usuario.objects.get(login=request.session['username'])
    user_id = usuario.id
    listas = Lista.objects.filter(user_id=user_id)
    context = {
        'usuario': usuario,
        'listas': listas
    }
    return render(request, 'usuarios/home_usuario.html', context)
