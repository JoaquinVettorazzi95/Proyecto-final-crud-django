from django.shortcuts import render, get_object_or_404
from ejemplo.models import Perros
from ejemplo.models import Personas
from ejemplo.models import Autos
from ejemplo.forms import BuscarPerros, BuscarPersonas, BuscarAutos, PerrosForm, PersonasForm, AutosForm
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView


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

class ActualizarPerro(View):
  form_class = PerrosForm
  template_name = 'ejemplo/actualizar_perro.html'
  initial = {"nombre":"", "raza":"", "edad":""}
  

  def get(self, request, pk): 
      perro = get_object_or_404(Perros, pk=pk)
      form = self.form_class(instance = perro)
      return render(request, self.template_name, {'form':form,'perro': perro})

  
  def post(self, request, pk): 
      perro = get_object_or_404(Perros, pk=pk)
      form = self.form_class(request.POST ,instance = perro)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el Perro {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'Perro': perro,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class ActualizarPersona(View):
  form_class = PersonasForm
  template_name = 'ejemplo/actualizar_persona.html'
  initial = {"nombre":"", "sexo":"", "dni":""}

  def get(self, request, pk): 
      persona = get_object_or_404(Personas, pk=pk)
      form = self.form_class(instance = persona)
      return render(request, self.template_name, {'form':form,'persona': persona})

  
  def post(self, request, pk): 
      persona = get_object_or_404(Personas, pk=pk)
      form = self.form_class(request.POST ,instance = persona)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito los datos de {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'persona': persona,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class ActualizarAuto(View):
  form_class = AutosForm
  template_name = 'ejemplo/actualizar_auto.html'
  initial = {"marca":"", "modelo":"", "matricula":""}

  def get(self, request, pk): 
      auto = get_object_or_404(Autos, pk=pk)
      form = self.form_class(instance = auto)
      return render(request, self.template_name, {'form':form,'auto': auto})

  
  def post(self, request, pk): 
      auto = get_object_or_404(Autos, pk=pk)
      form = self.form_class(request.POST ,instance = auto)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito los datos del auto con matricula {form.cleaned_data.get('matricula')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'Auto': auto,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarPerro(View):
  template_name = 'ejemplo/perros.html'

  def get(self, request, pk): 
      perro = get_object_or_404(Perros, pk=pk)
      perro.delete()
      perros = Perros.objects.all()
      return render(request, self.template_name, {'lista_perros': perros})

class BorrarPersona(View):
  template_name = 'ejemplo/personas.html'

  def get(self, request, pk): 
      persona = get_object_or_404(Personas, pk=pk)
      persona.delete()
      personas = Personas.objects.all()
      return render(request, self.template_name, {'lista_personas': personas})


class BorrarAuto(View):
  template_name = 'ejemplo/autos.html'

  def get(self, request, pk): 
      auto = get_object_or_404(Autos, pk=pk)
      auto.delete()
      autos = Autos.objects.all()
      return render(request, self.template_name, {'lista_autos': autos})


class PerrosList(ListView):
  model = Perros

class AutosList(ListView):
  model = Autos

class PersonasList(ListView):
  model = Personas

class PerrosCrear(CreateView):
  model = Perros
  success_url = "/panel_perros"
  fields = ["nombre", "raza", "edad"]

class AutosCrear(CreateView):
  model = Autos
  success_url = "/panel_autos"
  fields = ["marca", "modelo", "matricula"]

class PersonasCrear(CreateView):
  model = Personas
  success_url = "/panel_personas"
  fields = ["nombre", "sexo", "dni"]

class PerrosBorrar(DeleteView):
  model = Perros
  success_url = "/panel_perros"

class AutosBorrar(DeleteView):
  model = Autos
  success_url = "/panel_autos"

class PersonasBorrar(DeleteView):
  model = Personas
  success_url = "/panel_personas"

class PerrosActualizar(UpdateView):
  model = Perros
  success_url = "/panel_perros"
  fields = ["nombre", "raza", "edad"]

class AutosActualizar(UpdateView):
  model = Autos
  success_url = "/panel_autos"
  fields = ["marca", "modelo", "matricula"]

class PersonasActualizar(UpdateView):
  model = Personas
  success_url = "/panel_personas"
  fields = ["nombre", "sexo", "dni"]
