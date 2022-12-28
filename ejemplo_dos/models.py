from django.db import models
from django.contrib.auth.admin import User


class Post (models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    publicado_el = models.DateField()
    imagen = models.ImageField(upload_to='posteos', null=True, blank=True)

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='avatar')
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)