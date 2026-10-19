
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Rol


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('IdRol', 'NombreRol', 'Descripcion')
    search_fields = ('NombreRol',)


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = (
        'IdUsuario',
        'Correo',
        'Nombre',
        'Apellido',
        'IdRol',
        'is_staff',
        'is_active',
    )

    search_fields = ('Correo', 'Nombre', 'Apellido')
    list_filter = ('is_staff', 'is_active', 'IdRol')

    fieldsets = (
        ('Acceso', {
            'fields': ('Correo', 'password')
        }),
        ('Información personal', {
            'fields': ('Nombre', 'Apellido', 'Telefono', 'IdRol')
        }),
        ('Permisos', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )

    add_fieldsets = (
        ('Crear usuario', {
            'classes': ('wide',),
            'fields': (
                'Correo',
                'username',
                'Nombre',
                'Apellido',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

    ordering = ('Correo',)
    filter_horizontal = ('groups', 'user_permissions')
