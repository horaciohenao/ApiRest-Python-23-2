# API rest Python con Django

Este proyecto es para almacenar el codigo para una API rest hecha en Python con Django

Hecha por horacio henao 22/11/2023

# Requisitos minimos

- Python
- Git

# Como usar?

***PARA NO TENER QUE HACER PASO POR PASO PUEDE SIMPLEMENTE USAR EL SIGUIENTE COMANDO***
 ```
 git clone https://github.com/horaciohenao/ApiRest-Python-23-2.git && cd ApiRest-Python-23-2 && py -m venv .venv && .venv\Scripts\activate.bat && pip install django && pip install djangorestframework && py manage.py migrate && py manage.py createsuperuser && py manage.py runserver
 ```
 Igualmente debe rellenar los datos de la cuenta (más detalles en el paso 7) y al final abrir  [esta pagina](http://127.0.0.1:8000/admin/login/?next=/admin/)
 
 ## Guia completa

Para usar y ejeuctar esta db se deben usar los siguiente comandos

1. Usar el comando
 ```
 git clone https://github.com/horaciohenao/ApiRest-Python-23-2.git
 ```
 
2. Moverse al directorio apropiado
```
cd ApiRest-Python-23-2
```
 
3. Crear un entorno de python con 
```
 py -m venv .venv
```

4. Ejecutar el entorno
```
 .venv\Scripts\activate.bat
```

5. Descargar las librerias necesarias
```
pip install django && pip install djangorestframework
```

6. Comandos para solucionar posibles errores
```
py manage.py migrate
```

7. Se ejecuta el comando 
```
py manage.py createsuperuser
```
Esto para crear una cuenta de administrador de lo contrario nunca se podra administrar, para mantenerlo simple, use
```
user: admin
email: email@email.com
password: 1234
```

8. Ejecute el servidor
```
py manage.py runserver
```

9. LISTO! Ahora puede ver la pagina [administracion](http://127.0.0.1:8000/admin/login/?next=/admin/) solo use los datos creados anteriormente, para el login

P.D: Si desea ver cómo hacer POST o un GET mire mi [video](https://youtu.be/r341QJ1Q0eo) para ver como esta todo hecho