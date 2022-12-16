from django.shortcuts import render
from ejemplo.models import Perros
from ejemplo.models import Personas
from ejemplo.models import Autos
from ejemplo.forms import Buscar 
from django.views import View


def mostrar_perros(request):
  lista_perros = Perros.objects.all()
  return render(request, "ejemplo/perros.html", {"lista_perros": lista_perros})

def mostrar_personas(request):
  lista_personas = Personas.objects.all()
  return render(request, "ejemplo/personas.html", {"lista_personas": lista_personas})

def mostrar_autos(request):
  lista_autos = Autos.objects.all()
  return render(request, "ejemplo/autos.html", {"lista_autos": lista_autos})

class BuscarPerros(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_perros = Perros.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_perros':lista_perros})
        return render(request, self.template_name, {"form": form})