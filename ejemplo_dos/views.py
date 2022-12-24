from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy
from ejemplo_dos.forms import UsuarioForm



def index(request):
    return render(request, "ejemplo_dos/index.html", {})

class PostDetalle(ListView):
    model= Post

class PostListar(ListView):
    model = Post  
    
class PostCrear(CreateView):
    model= Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = '__all__'

class PostBorrar(DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")

class PostActualizar(UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('ejemplo-dos-listar')


