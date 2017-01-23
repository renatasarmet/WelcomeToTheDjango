from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *


# Create your views here.
def index(request):
    materias = Materia.objects.all()

    return render_to_response('hello/index.html', {'materias': materias})

@login_required(login_url='/login/')
def supersecret(request):
    return render_to_response('hello/supersecret.html', {})

def login(request):
    dict = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            usuario = User.objects.get(username=username)
            if usuario.is_active:
                usuario_autenticado = authenticate(username=username, password=password)
                if usuario_autenticado is not None:
                    django_login(request, usuario_autenticado)
                else:
                    dict['erro'] = "Usuário ou senha inválidos."

            else:
                dict['erro'] = "Usuário inativo."

        except:
            dict['erro'] = "Usuário ou senha inválidos."

    return render(request, 'hello/login.html', dict)

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)

    return HttpResponseRedirect('/')