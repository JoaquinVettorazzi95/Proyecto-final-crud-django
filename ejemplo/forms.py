from django import forms
from ejemplo.models import Perros
from ejemplo.models import Personas
from ejemplo.models import Autos

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=15)


class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)


class PerrosForm(forms.ModelForm):
  class Meta:
    model = Perros
    fields = ['nombre', 'raza', 'edad']

class PersonasForm(forms.ModelForm):
  class Meta:
    model = Personas
    fields = ['nombre', 'sexo', 'dni']

class AutosForm(forms.ModelForm):
  class Meta:
    model = Autos
    fields = ['marca', 'modelo', 'matricula']