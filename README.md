Sitio web realizado con DJango

Primero, corremos el proyecto utilizando python manage.py runserver, desde la terminal Bash.

Luego ingresa en el navegador : localhost:8000

Se pueden ingresar nuevos registros para los 3 tipos de datos:

- Perosonas (localhost:8000/mostrar_personas/alta), Perros (localhost:8000/mostrar_perros/alta), Autos (localhost:8000/mostrar_autos/alta).
    Se completan cada uno de los campos con los datos que se quieren crear y presionamos el botón "Ingresar". De esta forma quedarán ingresados en nuestra base de datos.

Si corremos en el navegador: 
    -localhost:8000/mostrar_personas, veremos toda nuestra base de datos de personas, y el nuevo registro al final.
    -localhost:8000/mostrar_perros, veremos toda nuestra base de datos de perros, y el nuevo registro al final.
    -localhost:8000/mostrar_autos, veremos toda nuestra base de datos de autos, y el nuevo registro al final.

Si ingresamos al navegador (localhost:8000/mostrar_perros/buscar), completamos el campo con el nombre del Perro y hacemos click en "Buscar", podremos buscar el perro en nuestra base de datos. De la misma forma se puede proceder con Personas (buscando por su nombre) y autos (buscando por su matricula)





`




