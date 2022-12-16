from django.shortcuts import render
from ejemplo.models import Perros
from ejemplo.models import Personas
from ejemplo.models import Autos


def mostrar_perros(request):
  lista_perros = Perros.objects.all()
  return render(request, "ejemplo/perros.html", {"lista_perros": lista_perros})

def mostrar_personas(request):
  lista_personas = Personas.objects.all()
  return render(request, "ejemplo/personas.html", {"lista_personas": lista_personas})

def mostrar_autos(request):
  lista_autos = Autos.objects.all()
  return render(request, "ejemplo/autos.html", {"lista_autos": lista_autos})