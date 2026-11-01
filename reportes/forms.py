from django import forms
from .models import ReporteAmbiental, Categoria

class ReporteAmbientalForm(forms.ModelForm):
    class Meta:
        model = ReporteAmbiental
        fields = [
            "Titulo",
            "Descripcion",
            "UbicacionReferencial",
            "IdCategoria",
        ]

        widgets = {
            "Titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej. Acumulación de basura",
            }),
            "Descripcion": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Describe el problema...",
            }),
            "UbicacionReferencial": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej. Calle principal, cerca del parque",
            }),
            "IdCategoria": forms.Select(attrs={
                "class": "form-select",
            }),
        }

        labels = {
            "Titulo": "Título del reporte",
            "Descripcion": "Descripción del problema",
            "UbicacionReferencial": "Ubicación del problema",
            "IdCategoria": "Categoría ambiental",
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["NombreCategoria", "Descripcion"]

        widgets = {
            "NombreCategoria": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "Descripcion": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
            }),
        }

        labels = {
            "NombreCategoria": "Nombre de la categoría",
            "Descripcion": "Descripción",
        }