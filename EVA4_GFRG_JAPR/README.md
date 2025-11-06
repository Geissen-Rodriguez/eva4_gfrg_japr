
para restaurar base de datos con dump.sql

Para cargar la base de datos completa con el superusuario ya creado:

* primero Clonar el repositorio:

* segundo crear la base vacía en pgAdmin: eva4_gfrg_japr

* tercero restaurar el dump

ejecutar:

psql -U postgres -d eva4_gfrg_japr < dump.sql



Usuario: admin1
Contraseña: geissen2025
Correo: admin1@prueba.com


configurar settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eva4_gfrg_japr',          
        'USER': 'postgres',                 
        'PASSWORD': '12345', 
        'HOST': 'localhost',
        'PORT': '5432',
    }
}