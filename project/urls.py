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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ejemplo.views import (mostrar_perros, mostrar_personas, mostrar_autos, BuscarPerro, BuscarPersona , BuscarAuto, AltaPerros, AltaPersonas, AltaAutos,
ActualizarPerro, ActualizarPersona, ActualizarAuto, BorrarPerro, BorrarPersona, BorrarAuto, PerrosList, AutosList, PersonasList, PerrosBorrar, 
PerrosCrear, AutosCrear, PersonasCrear, AutosBorrar, PersonasBorrar, PerrosActualizar, AutosActualizar, PersonasActualizar)
from mi_blog.views import (index,PostCrear, PostDetalle, PostListar, PostBorrar, PostActualizar, UserSignUp, UserLogin, 
UserLogout, AvatarActualizar, UserActualizar, MensajeBorrar, MensajeCrear, MensajeDetalle, MensajeListar)
from django.contrib.admin.views.decorators import staff_member_required





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
    path('mi-blog/',index, name='mi-blog-index'),
    path('mi-blog/crear/',staff_member_required (PostCrear.as_view()),name='mi-blog-crear'),
    path('mi-blog/<int:pk>/detalle/', PostDetalle.as_view(), name="mi-blog-detalle"),
    path('mi-blog/listar/', PostListar.as_view(), name="mi-blog-listar"),
    path('mi-blog/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="mi-blog-borrar"),
    path('mi-blog/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="mi-blog-actualizar"),
    path('mi-blog/signup/', UserSignUp.as_view(), name ="mi-blog-signup"),
    path('mi-blog/login/', UserLogin.as_view(), name= "mi-blog-login"),
    path('mi-blog/logout/', UserLogout.as_view(), name="mi-blog-logout"),
    path('mi-blog/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="mi-blog-users-actualizar"),
    path('mi-blog/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="mi-blog-avatars-actualizar"),
    path('mi-blog/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="mi-blog-mensajes-borrar"),
    path('mi-blog/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="mi-blog-mensajes-detalle"),
    path('mi-blog/mensajes/listar/', MensajeListar.as_view(), name="mi-blog-mensajes-listar"),
    path('mi-blog/mensajes/crear/', MensajeCrear.as_view(), name="mi-blog-mensajes-crear"),
]



urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)