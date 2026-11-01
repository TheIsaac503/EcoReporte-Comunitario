from django.contrib import admin
from django.urls import path, include
from reportes import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("reportes/", include("reportes.urls")),
    path("tablas/", views.vista_tablas, name="vista_tablas"),
]
