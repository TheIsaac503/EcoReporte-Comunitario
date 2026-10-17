from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tablas/', views.vista_tablas, name='vista_tablas'),
]