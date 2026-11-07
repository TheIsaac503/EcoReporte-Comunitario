#!/usr/bin/env bash

# Detener el despliegue si ocurre algún error
set -o errexit

# Instalar las dependencias
pip install -r requirements.txt

# Preparar los archivos estáticos
python manage.py collectstatic --no-input

# Aplicar las migraciones de Django
python manage.py migrate --noinput

# Crear superusuario automáticamente si no existe
if [ "$CREATE_SUPERUSER" = "true" ]; then
  python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superusuario '{username}' creado exitosamente.")
    else:
        print(f"El superusuario '{username}' ya existe.")
EOF
fi