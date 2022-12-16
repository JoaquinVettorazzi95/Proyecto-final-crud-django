from django.db import models

class Perros(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.raza}, {self.id}"

class Personas(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dni = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.sexo}, {self.dni}"

class Autos(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)
    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.matricula}"