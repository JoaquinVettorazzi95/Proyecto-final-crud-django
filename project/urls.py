"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (mostrar_perros, mostrar_personas, mostrar_autos, BuscarPerro, BuscarPersona , BuscarAuto, AltaPerros, AltaPersonas, AltaAutos,
ActualizarPerro, ActualizarPersona, ActualizarAuto, BorrarPerro, BorrarPersona, BorrarAuto, PerrosList, AutosList, PersonasList, PerrosBorrar, 
PerrosCrear, AutosCrear, PersonasCrear, AutosBorrar, PersonasBorrar, PerrosActualizar, AutosActualizar, PersonasActualizar)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mostrar_perros/', mostrar_perros),
    path('mostrar_personas/', mostrar_personas),
    path('mostrar_autos/', mostrar_autos),
    path('mostrar_perros/buscar', BuscarPerro.as_view()),
    path('mostrar_personas/buscar', BuscarPersona.as_view()),
    path('mostrar_autos/buscar', BuscarAuto.as_view()),   
    path('mostrar_perros/alta', AltaPerros.as_view()),
    path('mostrar_personas/alta', AltaPersonas.as_view()),
    path('mostrar_autos/alta', AltaAutos.as_view()),
    path('mostrar_perros/actualizar/<int:pk>', ActualizarPerro.as_view()),
    path('mostrar_personas/actualizar/<int:pk>', ActualizarPersona.as_view()),
    path('mostrar_autos/actualizar/<int:pk>', ActualizarAuto.as_view()),
    path('mostrar_perros/borrar/<int:pk>', BorrarPerro.as_view()),
    path('mostrar_personas/borrar/<int:pk>', BorrarPersona.as_view()),
    path('mostrar_autos/borrar/<int:pk>', BorrarAuto.as_view()),
    path('panel_perros/', PerrosList.as_view()),
    path('panel_autos/', AutosList.as_view()),
    path('panel_personas/', PersonasList.as_view()),
    path('panel_perros/crear', PerrosCrear.as_view()),
    path('panel_autos/crear', AutosCrear.as_view()),
    path('panel_personas/crear', PersonasCrear.as_view()),
    path('panel_perros/<int:pk>/borrar', PerrosBorrar.as_view()),
    path('panel_autos/<int:pk>/borrar', AutosBorrar.as_view()),
    path('panel_personas/<int:pk>/borrar', PersonasBorrar.as_view()),
    path('panel_perros/<int:pk>/actualizar', PerrosActualizar.as_view()),
    path('panel_autos/<int:pk>/actualizar', AutosActualizar.as_view()),
    path('panel_personas/<int:pk>/actualizar', PersonasActualizar.as_view()),
]
