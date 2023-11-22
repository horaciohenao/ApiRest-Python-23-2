# API rest Python

Este proyecto es para almacenar una API rest hecha en Python con Django

## Como usar?

## Proceso de desarrollo

### Crear entorno

- Para empezar cree una entorno virtual en Py con ``py -m venv .venv``

- Luego usando ``.venv\Scripts\activate.bat`` inicio este mismo

- Ahora se instala ``django`` con ``pip install django`` y ``pip install djangorestframework``, ahora esperamos que el proceso termine

***Esto para que se instale solo en el entorno de desarrollo.***

- para crear el proyect se usa ``django-admin startproject Mi_API_rest .``

- esto crea los archivos necesarios para ejecutar el proyecto

### iniciar el entorno

- ahora con ``py manage.py runserver`` se inicia el servidor en el host privado 

- y este seria el resultado
![](https://i.imgur.com/OOSuYny.png)

### administrar db

- ahora debemos entrar a la db, un modo seria como administrador pero esta no tiene cuentas ni datos aun. Podemos usar en una nueva terminal y ejecutamos los siguientes comandos
```py
py manage.py migrate
py manage.py createsuperuser
```
Este es el resultado, esto para arreglar errores y crear un usuario

![](https://i.imgur.com/8Mtsrcy.png)

Ahora podemos administrar la db!

![](https://i.imgur.com/cDCxgW3.png)

### crear tablas 

- ahora creamos un archivo ``models.py`` (solo por comodidad) el cual contiene la estructura de nuestras tablas, en este especificamos las caracteristicas de nuestra tabla, y para agregar esta a nuestra api cambiamos el archivo llamado ``settings.py`` para agregar nuestra db en la seccion ``INSTALLED_APPS``, agregamos el nombre de nuestra db, y ejecutamos los siguientes comndos

```
py manage.py makemigrations Mi_API_rest
py manage.py migrate
```

- finalmente para mostrar nuestra tabla creamos una archivo ``admin.py`` para registrar nuestra tabla nueva, para esto se debe reiniciar el server para ver los cambios
<!-- ![](https://i.imgur.com/4gfYT8o.png) -->

***A ESTE PUNTO LA DB ESTA FUNCIONANDO CORRECTAMENTE***

### crear la api

- ahora en ``settings.py``, nuevamente agregamos ``rest_framework`` y crear un archivo ``serializers`` este para menejar respuestas json

- dentro de este vamos a usar serializers, que segun foros,  los serializers son objetos que se utilizan para convertir objetos de Django en formatos de datos serializables, como JSON, XML o CSV. También se pueden utilizar para convertir datos serializados en objetos de Django.

- con los campos que son las caracteristicas de nuestra tabla creada

- ahora se crea ``views.py`` el cual convierte los valores de la tabla a una respuesta json

***A ESTE PUNTO LA API FUNCIONA PERFECTAMENTE***

### como hacer un post

- para esto podemos usar postman y especificar nuestra url, más detalles en el video así como la explicaion completa