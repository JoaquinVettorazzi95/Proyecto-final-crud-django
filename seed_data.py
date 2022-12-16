from ejemplo.models import Perros
from ejemplo.models import Personas
from ejemplo.models import Autos


Perros(nombre="Roco", raza="Rottweiler", edad=4).save()
Perros(nombre="Mili", raza="Pug", edad=6).save()
Perros(nombre="Toto", raza="Maltez", edad=1).save()
Perros(nombre="Ringo", raza="Caniche", edad=2).save()
Perros(nombre="Benja", raza="Chiwawa", edad=8).save()
Perros(nombre="Inti", raza="Caniche", edad=11).save()


print("Se cargo con éxito los usuarios de pruebas")



Personas(nombre="Joaco", sexo="Scoseria 2933", dni=123123343).save()
Personas(nombre="Jose", sexo="Silvan 2955", dni=123123343).save()
Personas(nombre="Joaco", sexo="Rodo 2533", dni=123123343).save()

print("Se cargo con éxito los usuarios de pruebas")


Autos(marca="Ford", modelo="GT", matricula="AA3242").save()
Autos(marca="Subaru", modelo="A45", matricula="AA4443").save()
Autos(marca="Jeep", modelo="Adventure", matricula="AB2342").save()
Autos(marca="Ford", modelo="Fiesta", matricula="AX2424").save()

print("Se cargo con éxito los usuarios de pruebas")gi