from django.shortcuts import render, redirect
from .forms import ComentarioForm

# Usuarios simulados
USUARIOS = {
    "admin": "1234",
    "jossie": "ugb2024",
    "prueba": "prueba123",
}

def login_usuario(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username in USUARIOS and USUARIOS[username] == password:
            return redirect(
                "https://pagina-tienda-huella-hurbana.notion.site/"
                "Huella-Urbana-29c1ac9afb7b802e83bac4d5b06253d9"
            )
        else:
            error = "Usuario o contraseña incorrectos"

    return render(request, "login.html", {"error": error})

def registro_usuario(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username in USUARIOS:
            error = "El usuario ya existe"
        else:
            USUARIOS[username] = password
            return redirect('login')

    return render(request, "registro.html", {"error": error})

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pagina, Comentario
from .forms import ComentarioForm
from django.contrib.auth.decorators import login_required

@login_required
def pagina_detalle(request, pk):
    pagina = get_object_or_404(Pagina, pk=pk)
    comentarios = pagina.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.pagina = pagina
            comentario.autor = request.user
            comentario.bloque = comentarios.count() + 1  # Se asigna número de bloque
            comentario.save()
            return redirect('pagina_detalle', pk=pagina.pk)
    else:
        form = ComentarioForm()

    return render(request, 'pagina_detalle.html', {'pagina': pagina, 'comentarios': comentarios, 'form': form})


# Create your views here.
