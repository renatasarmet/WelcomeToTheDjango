from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse

from .models import *


# Create your views here.
def index(request):
    materias = Materia.objects.all()

    return render_to_response('hello/index.html', {'materias': materias})
