from django.contrib import admin
from django.urls import path, include
from reportes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("reportes/", include("reportes.urls")),
    path("tablas/", views.vista_tablas, name="vista_tablas"),
    
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )