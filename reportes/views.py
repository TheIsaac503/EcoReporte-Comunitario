from django.shortcuts import render
from .models import Rol, Usuario, Categoria, ReporteAmbiental, EvidenciaFotografia, HistorialEstado

def home(request):
    """
    Vista principal de inicio y diagnóstico.
    """
    context = {
        'total_reportes': ReporteAmbiental.objects.count(),
        'reportes_pendientes': ReporteAmbiental.objects.filter(Estado='Pendiente').count(),
        'total_usuarios': Usuario.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'comunidad': 'Caserío El Tule, Canton Potrero Grande, El Paisnal'
    }
    return render(request, 'reportes/home.html', context)

def vista_tablas(request):
    """
    Vista general para consultar los registros almacenados en las 6 tablas de SQL Server.
    """
    context = {
        'roles': Rol.objects.all(),
        'usuarios': Usuario.objects.all(),
        'categorias': Categoria.objects.all(),
        'reportes': ReporteAmbiental.objects.all(),
        'evidencias': EvidenciaFotografia.objects.all(),
        'historiales': HistorialEstado.objects.all(),
    }
    return render(request, 'reportes/lista_tablas.html', context)