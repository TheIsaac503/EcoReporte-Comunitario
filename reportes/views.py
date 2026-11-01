from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from usuarios.models import Usuario, Rol
from .forms import ReporteAmbientalForm, CategoriaForm
from .models import Categoria, ReporteAmbiental, EvidenciaFotografia, HistorialEstado


def es_administrador(user):
    # is_staff habilita las funciones de gestión del sistema.
    return user.is_authenticated and user.is_staff


def home(request):
    context = {
        "total_reportes": ReporteAmbiental.objects.count(),
        "reportes_pendientes": ReporteAmbiental.objects.filter(Estado="Pendiente").count(),
        "total_usuarios": Usuario.objects.count(),
        "total_categorias": Categoria.objects.count(),
        "comunidad": "Caserío El Tule, Cantón Potrero Grande, El Paisnal",
    }
    return render(request, "reportes/home.html", context)


@login_required
def vista_tablas(request):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {
        "roles": Rol.objects.all(),
        "usuarios": Usuario.objects.all(),
        "categorias": Categoria.objects.all(),
        "reportes": ReporteAmbiental.objects.select_related("IdUsuario", "IdCategoria"),
        "evidencias": EvidenciaFotografia.objects.all(),
        "historiales": HistorialEstado.objects.all(),
    }
    return render(request, "reportes/lista_tablas.html", context)


@login_required
def crear_reporte(request):
    if request.method == "POST":
        formulario = ReporteAmbientalForm(request.POST)
        if formulario.is_valid():
            reporte = formulario.save(commit=False)
            reporte.IdUsuario = request.user
            reporte.Estado = "Pendiente"
            reporte.save()
            messages.success(request, "¡Tu reporte ambiental se registró correctamente!")
            return redirect("listar_reportes")
    else:
        formulario = ReporteAmbientalForm()
    return render(request, "reportes/crear_reporte.html", {
        "formulario": formulario, "titulo_pagina": "Registrar reporte",
    })


def listar_reportes(request):
    reportes = ReporteAmbiental.objects.select_related(
        "IdUsuario", "IdCategoria"
    ).order_by("-FechaCreacion")
    return render(request, "reportes/listar_reportes.html", {"reportes": reportes})


@login_required
def editar_reporte(request, pk):
    reporte = get_object_or_404(
        ReporteAmbiental.objects.select_related("IdUsuario"), pk=pk
    )
    if reporte.IdUsuario_id != request.user.pk and not request.user.is_staff:
        raise PermissionDenied
    if request.method == "POST":
        formulario = ReporteAmbientalForm(request.POST, instance=reporte)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El reporte se actualizó correctamente.")
            return redirect("listar_reportes")
    else:
        formulario = ReporteAmbientalForm(instance=reporte)
    return render(request, "reportes/crear_reporte.html", {
        "formulario": formulario, "titulo_pagina": "Modificar reporte",
        "es_edicion": True,
    })


@login_required
def eliminar_reporte(request, pk):
    reporte = get_object_or_404(
        ReporteAmbiental.objects.select_related("IdUsuario"), pk=pk
    )
    if reporte.IdUsuario_id != request.user.pk and not request.user.is_staff:
        raise PermissionDenied
    if request.method == "POST":
        reporte.delete()
        messages.success(request, "El reporte se eliminó correctamente.")
        return redirect("listar_reportes")
    return render(request, "reportes/confirmar_eliminacion.html", {
        "objeto": reporte, "tipo": "reporte",
    })


@login_required
@user_passes_test(es_administrador)
def listar_categorias(request):
    categorias = Categoria.objects.all().order_by("NombreCategoria")
    return render(request, "reportes/listar_categorias.html", {"categorias": categorias})


@login_required
@user_passes_test(es_administrador)
def crear_categoria(request):
    if request.method == "POST":
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La categoría se creó correctamente.")
            return redirect("listar_categorias")
    else:
        formulario = CategoriaForm()
    return render(request, "reportes/formulario_categoria.html", {
        "formulario": formulario, "titulo": "Nueva categoría",
    })


@login_required
@user_passes_test(es_administrador)
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        formulario = CategoriaForm(request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La categoría se actualizó correctamente.")
            return redirect("listar_categorias")
    else:
        formulario = CategoriaForm(instance=categoria)
    return render(request, "reportes/formulario_categoria.html", {
        "formulario": formulario, "titulo": "Modificar categoría",
    })


@login_required
@user_passes_test(es_administrador)
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        try:
            categoria.delete()
            messages.success(request, "La categoría se eliminó correctamente.")
        except Exception:
            messages.error(
                request,
                "No se puede eliminar esta categoría porque tiene reportes asociados."
            )
        return redirect("listar_categorias")
    return render(request, "reportes/confirmar_eliminacion.html", {
        "objeto": categoria, "tipo": "categoría",
    })
