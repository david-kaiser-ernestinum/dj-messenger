from django.shortcuts import render    
from django.shortcuts import redirect

from django.contrib.auth.models import User 
from django.contrib.auth import authenticate #django auth methoden
from django.contrib.auth import login
from django.contrib.auth import logout

# Funktion für die Registrierung
def register_view(request):

    error = ""
    
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        
        # Keine Benutzernamen kommen mehrfach vor
        if User.objects.filter(
                username=username 
            ).exists():
            
            error = "Benutzername exisitiert bereits"
    
        # Bei erfolgreicher erstellung eines Accounts wird auf die Home-Seite weitergeleitet
        else:
            user = User.objects.create_user(
                    username=username,
                    password=password
                    )

            # Sicheres Anmelden durch die Django-Methode
            login(request,user)

            return redirect("/home/")
    
    # Bei einer fehlgeschlagenen Registrierung oder beim aufrufen der Seite
    return render(
            request,
            "register.html",
            {"error": error})

# Funktion für das Anmelden
def login_view(request):

    error = "" 
    
    # wenn gepostet wird, werden die Daten aus der Anfrage extrahiert
    if request.method == "POST": 
        username = request.POST["username"] 
        password = request.POST["password"]


        user = authenticate(request, 
                            username=username,
                            password=password
                            )

        # Wenn der Nutzer existiert und die Daten stimmen wird er auf die Home-Seite weitergeleitet
        if user:
            login(
                    request,
                    user
                    )

            return redirect("/home/")


        error = "Falscher Login"

    # Bei einer fehlgeschlagenen Anmeldung oder beim aufrufen der Seite
    return render(
            request,
            "login.html",
            {
                "error":error
            })

# Beim Abmelden wird auf die Startseite verwiesen
def logout_view(request):
    logout(request)

    return redirect("/index/") 










