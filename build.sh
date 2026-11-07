#!/usr/bin/env bash

# Detener el despliegue si ocurre algún error
set -o errexit

# Instalar las dependencias
pip install -r requirements.txt

# Preparar los archivos estáticos
python manage.py collectstatic --no-input

# Aplicar las migraciones de Django
python manage.py migrate --noinput

# Crear superusuario personalizado
if [ "$CREATE_SUPERUSER" = "true" ]; then
  python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()

# Variables de entorno
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'adescoadmin@gmail.com')
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'EltuleSA503')

if email and password:
    if not User.objects.filter(Correo=email).exists():
        User.objects.create_superuser(
            Correo=email,
            password=password,
            username=username,
            Nombre='Admin',
            Apellido='Sistema'
        )
        print(f"Superusuario con correo '{email}' creado exitosamente.")
    else:
        print(f"El superusuario con correo '{email}' ya existe.")
EOF
fi