
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReporteAmbientalForm
from usuarios.models import Usuario, Rol
from .models import (
    Categoria,
    ReporteAmbiental,
    EvidenciaFotografia,
    HistorialEstado,
)


def inicio(request):
    return render(request, 'reportes/inicio.html')


def home(request):
    """
    Vista principal de inicio y diagnóstico.
    """
    context = {
        'total_reportes': ReporteAmbiental.objects.count(),
        'reportes_pendientes': ReporteAmbiental.objects.filter(
            Estado='Pendiente'
        ).count(),
        'total_usuarios': Usuario.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'comunidad': 'Caserío El Tule, Canton Potrero Grande, El Paisnal',
    }

    return render(request, 'reportes/home.html', context)


def vista_tablas(request):
    """
    Vista general para consultar los registros almacenados
    en las tablas de SQL Server.
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

@login_required
def crear_reporte(request):
    if request.method == 'POST':
        formulario = ReporteAmbientalForm(request.POST)

        if formulario.is_valid():
            reporte = formulario.save(commit=False)
            reporte.IdUsuario = request.user
            reporte.Estado = 'Pendiente'
            reporte.save()

            messages.success(
                request,
                '¡Tu reporte ambiental se registró correctamente!'
            )

            return redirect('crear_reporte')
    else:
        formulario = ReporteAmbientalForm()

    return render(
        request,
        'reportes/crear_reporte.html',
        {'formulario': formulario}
    )


def listar_reportes(request):
    reportes = ReporteAmbiental.objects.select_related(
        'IdUsuario',
        'IdCategoria'
    ).order_by('-FechaCreacion')

    return render(
        request,
        'reportes/listar_reportes.html',
        {'reportes': reportes}
    )
