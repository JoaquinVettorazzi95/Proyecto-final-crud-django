from ejemplo.models import Perros

Perros(nombre="Roco", raza="Rottweiler", edad=4).save()
Perros(nombre="Mili", raza="Pug", edad=6).save()
Perros(nombre="Toto", raza="Maltez", edad=1).save()
Perros(nombre="Ringo", raza="Caniche", edad=2).save()
Perros(nombre="Benja", raza="Chiwawa", edad=8).save()
Perros(nombre="Inti", raza="Caniche", edad=11).save()


print("Se cargo con éxito los usuarios de pruebas")