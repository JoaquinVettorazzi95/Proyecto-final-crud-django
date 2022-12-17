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
from ejemplo.views import mostrar_perros, mostrar_personas, mostrar_autos, BuscarPerros, AltaPerros, AltaPersonas, AltaAutos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mostrar_perros/', mostrar_perros),
    path('mostrar_personas/', mostrar_personas),
    path('mostrar_autos/', mostrar_autos),
    path('mostrar_perros/buscar', BuscarPerros.as_view()), 
    path('mostrar_perros/alta', AltaPerros.as_view()),
    path('mostrar_personas/alta', AltaPersonas.as_view()),
    path('mostrar_autos/alta', AltaAutos.as_view()),

]
