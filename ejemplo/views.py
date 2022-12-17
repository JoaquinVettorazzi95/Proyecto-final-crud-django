from django.shortcuts import render
from ejemplo.models import Perros
from ejemplo.models import Personas
from ejemplo.models import Autos
from ejemplo.forms import BuscarPerros, BuscarPersonas, BuscarAutos, PerrosForm, PersonasForm, AutosForm
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

class BuscarPerro(View):
    form_class = BuscarPerros
    template_name = 'ejemplo/buscar_perros.html'
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

class BuscarPersona(View):
    form_class = BuscarPersonas
    template_name = 'ejemplo/buscar_personas.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_personas = Personas.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_personas':lista_personas})
        return render(request, self.template_name, {"form": form})

class BuscarAuto(View):
    form_class = BuscarAutos
    template_name = 'ejemplo/buscar_autos.html'
    initial = {"matricula":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            matricula = form.cleaned_data.get("matricula")
            lista_autos = Autos.objects.filter(matricula__icontains=matricula).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_autos':lista_autos})
        return render(request, self.template_name, {"form": form})


class AltaPerros(View):

    form_class = PerrosForm
    template_name = 'ejemplo/alta_perros.html'
    initial = {"nombre":"", "raza":"", "edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito el nuevo perro llamado {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})




class AltaPersonas(View):

    form_class = PersonasForm
    template_name = 'ejemplo/alta_personas.html'
    initial = {"nombre":"", "sexo":"", "dni":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito la nueva persona llamada {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaAutos(View):

    form_class = AutosForm
    template_name = 'ejemplo/alta_autos.html'
    initial = {"marca":"", "modelo":"", "matricula":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el nuevo ingreso del auto {form.cleaned_data.get('marca')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
