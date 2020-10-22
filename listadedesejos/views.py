from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, cookie
from usuarios.models import Usuario
from django.core.exceptions import ObjectDoesNotExist


# Código para um futuro próximo
# class LoginForm(forms.Form):
#     login = forms.CharField(max_length=40)
#     password = forms.CharField(max_length=40)


#
# View para mostrar a landing page
# 
def index(request):
    return render(request, 'listadedesejos/index.html')


#
# View para processar o login
#
def login(request):
    if request.method == 'GET':
        return render(request, template_name='listadedesejos/login.html')
    elif request.method == 'POST':
        # Obtendo os dados do formulário
        login = request.POST.get('login')
        senha = request.POST.get('password')

        # Recuperando o usuário no banco de dados através do campo login
        try:
            usuario = Usuario.objects.get(login=login)
            # Se o login for encontrado, então validar a senha.
            if usuario.senha == senha:
                # TO DO redirecionar para a página do usuário.
                request.session['username'] = login
                request.session['auth'] = True
                return HttpResponseRedirect('/listas/listar_listas')
            else:
                return HttpResponse('Usuario ou senha inválidos!')
        except ObjectDoesNotExist:
            return HttpResponse('Usuario não encontrado!')


#
# Logout do usuário
#
def logout(request):
    del request.session['username']
    del request.session['auth']
    return HttpResponseRedirect('/')