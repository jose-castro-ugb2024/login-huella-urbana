from django.shortcuts import render, redirect

# Usuarios simulados (Render Free)
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

# Create your views here.
