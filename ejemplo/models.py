from django.db import models

class Perros(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.raza}, {self.id}"