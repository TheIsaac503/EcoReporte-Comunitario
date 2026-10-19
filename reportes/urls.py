from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_reporte, name='crear_reporte'),
    path('lista/', views.listar_reportes, name='listar_reportes'),
]
