
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError


# Administrador personalizado para autenticar con Correo
class AdministradorUsuario(BaseUserManager):

    def create_user(self, Correo, password=None, **extra_fields):
        if not Correo:
            raise ValueError('El correo electrónico es obligatorio.')

        Correo = self.normalize_email(Correo)

        usuario = self.model(Correo=Correo, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, Correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(Correo, password, **extra_fields)


# Modelo Rol
class Rol(models.Model):
    IdRol = models.AutoField(primary_key=True, db_column='IdRol')
    NombreRol = models.CharField(max_length=50, unique=True, db_column='NombreRol')
    Descripcion = models.CharField(max_length=250, db_column='Descripcion')

    class Meta:
        db_table = 'Roles'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.NombreRol


# Modelo Usuario
class Usuario(AbstractUser):
    first_name = None
    last_name = None
    email = None

    objects = AdministradorUsuario()

    IdUsuario = models.AutoField(primary_key=True, db_column='IdUsuario')
    Nombre = models.CharField(max_length=50, db_column='Nombre')
    Apellido = models.CharField(max_length=60, db_column='Apellido')
    Correo = models.EmailField(max_length=150, unique=True, db_column='Correo')
    Telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        db_column='Telefono'
    )
    FechaRegistro = models.DateTimeField(
        auto_now_add=True,
        db_column='FechaRegistro'
    )
    Activo = models.BooleanField(default=True, db_column='Activo')

    IdRol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT,
        db_column='IdRol',
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'Correo'
    REQUIRED_FIELDS = ['username', 'Nombre', 'Apellido']

    class Meta:
        db_table = 'Usuarios'

    @property
    def nombre_completo(self):
        return f"{self.Nombre} {self.Apellido}".strip()

    def es_administrador(self):
        return bool(
            self.IdRol
            and self.IdRol.NombreRol.lower()
            in ['admin', 'administrador', 'adesco']
        )

    def clean(self):
        super().clean()

        if self.Telefono and not self.Telefono.replace('-', '').replace(' ', '').isdigit():
            raise ValidationError({
                'Telefono': 'El formato de teléfono debe contener únicamente números y guiones.'
            })

    def __str__(self):
        return f"{self.nombre_completo} ({self.Correo})"
