from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_reportes, name="inicio"),
    path("crear/", views.crear_reporte, name="crear_reporte"),
    path("lista/", views.listar_reportes, name="listar_reportes"),
    path("<int:pk>/editar/", views.editar_reporte, name="editar_reporte"),
    path("<int:pk>/eliminar/", views.eliminar_reporte, name="eliminar_reporte"),
    path("categorias/", views.listar_categorias, name="listar_categorias"),
    path("categorias/crear/", views.crear_categoria, name="crear_categoria"),
    path("categorias/<int:pk>/editar/", views.editar_categoria, name="editar_categoria"),
    path("categorias/<int:pk>/eliminar/", views.eliminar_categoria, name="eliminar_categoria"),
]
