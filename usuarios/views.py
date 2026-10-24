
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm


def registrar_usuario(request):
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                '¡Tu cuenta se creó correctamente! Ya puedes iniciar sesión.'
            )

            return redirect('login')
    else:
        formulario = RegistroUsuarioForm()

    return render(
        request,
        'usuarios/registro.html',
        {'formulario': formulario}
    )
