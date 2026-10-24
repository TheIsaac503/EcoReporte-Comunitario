
from django import forms
from django.utils.text import slugify
from .models import Usuario


class RegistroUsuarioForm(forms.Form):
    Nombre = forms.CharField(max_length=50, label="Nombre")
    Apellido = forms.CharField(max_length=60, label="Apellido")

    Correo = forms.EmailField(label="Correo electrónico")

    Telefono = forms.CharField(
        max_length=20,
        required=False,
        label="Teléfono"
    )

    password1 = forms.CharField(
        label="Contraseña",
        min_length=8,
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput
    )

    def clean_Correo(self):
        correo = self.cleaned_data['Correo'].strip()
        if Usuario.objects.filter(Correo__iexact=correo).exists():
            raise forms.ValidationError(
                "Este correo electrónico ya está registrado."
            )
        return correo

    def clean_Telefono(self):
        telefono = self.cleaned_data.get('Telefono', '').strip()

        if telefono and not telefono.replace('-', '').replace(' ', '').isdigit():
            raise forms.ValidationError(
                "El teléfono debe contener números y guiones."
            )

        return telefono

    def clean(self):
        datos = super().clean()

        password1 = datos.get('password1')
        password2 = datos.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error(
                'password2',
                "Las contraseñas no coinciden."
            )

        return datos

    def save(self):
        datos = self.cleaned_data
        correo = datos['Correo'].strip()

        # Generar un username único automáticamente.
        base = slugify(correo.split('@')[0]) or 'usuario'
        username = base
        contador = 1

        while Usuario.objects.filter(username=username).exists():
            username = f"{base}{contador}"
            contador += 1

        usuario = Usuario.objects.create_user(
            Correo=correo,
            password=datos['password1'],
            username=username,
            Nombre=datos['Nombre'],
            Apellido=datos['Apellido'],
            Telefono=datos.get('Telefono') or None,
            Activo=True
        )

        return usuario
