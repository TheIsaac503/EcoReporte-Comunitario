from django.contrib import admin
from .models import (
    Categoria,
    ReporteAmbiental,
    EvidenciaFotografia,
    HistorialEstado,
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('IdCategoria', 'NombreCategoria', 'Descripcion')
    search_fields = ('NombreCategoria',)


@admin.register(ReporteAmbiental)
class ReporteAmbientalAdmin(admin.ModelAdmin):
    list_display = (
        'IdReporteAmbiental',
        'Titulo',
        'Estado',
        'IdUsuario',
        'IdCategoria',
    )
    list_filter = ('Estado', 'IdCategoria')
    search_fields = ('Titulo', 'Descripcion', 'UbicacionReferencial')


@admin.register(EvidenciaFotografia)
class EvidenciaFotografiaAdmin(admin.ModelAdmin):
    list_display = (
        'IdEvidenciaFotografia',
        'RutaArchivo',
        'FechaCarga',
        'IdReporteAmbiental',
    )


@admin.register(HistorialEstado)
class HistorialEstadoAdmin(admin.ModelAdmin):
    list_display = (
        'IdHistorialEstado',
        'EstadoAnterior',
        'EstadoNuevo',
        'FechaCambio',
        'IdReporteAmbiental',
        'IdUsuarioAdmin',
    )
