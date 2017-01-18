from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    pessoa = {
        'nome': 'Marcelo',
        'sobrenome': 'de Oliveira'
    }

    materias = [
        'ED',
        'CAP',
        'Cálculo',
        'Django',
        "Web"
    ]

    return render_to_response('hello/index.html', {'pessoa': pessoa, 'materias': materias})
