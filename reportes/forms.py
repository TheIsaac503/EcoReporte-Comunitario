
from django import forms
from .models import ReporteAmbiental


class ReporteAmbientalForm(forms.ModelForm):

    class Meta:
        model = ReporteAmbiental

        fields = [
            'Titulo',
            'Descripcion',
            'UbicacionReferencial',
            'IdCategoria',
        ]

        widgets = {
            'Titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Acumulación de basura',
            }),

            'Descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe el problema ambiental...',
            }),

            'UbicacionReferencial': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Indica dónde ocurre el problema',
            }),

            'IdCategoria': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

        labels = {
            'Titulo': 'Título del reporte',
            'Descripcion': 'Descripción del problema',
            'UbicacionReferencial': 'Ubicación del problema',
            'IdCategoria': 'Categoría ambiental',
        }
