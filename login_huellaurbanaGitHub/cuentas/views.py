from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_usuario(request):
    if request.method == "POST":
        usuario = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            login(request, user)
            return redirect("https://pagina-tienda-huella-hurbana.notion.site/Huella-Urbana-29c1ac9afb7b802e83bac4d5b06253d9")
    
    return render(request, "login.html")



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def registro_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return redirect("registro")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        return redirect("login")

    return render(request, "registro.html")

def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(
                "https://pagina-tienda-huella-hurbana.notion.site/"
                "Huella-Urbana-29c1ac9afb7b802e83bac4d5b06253d9"
            )
        else:
            messages.error(request, "Credenciales incorrectas")

    return render(request, "login.html")


# Create your views here.
