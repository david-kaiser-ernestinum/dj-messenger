from django.shortcuts import render    #django standart biblotheken für weiterleitungen
from django.shortcuts import redirect
from django.contrib.auth.models import User #User datenbank von django

from django.contrib.auth import authenticate #django auth methoden
from django.contrib.auth import login
from django.contrib.auth import logout

def register_view(request): #registrieren

    error = "" #fehler platzhalter

    if request.method == "POST": #Als POST request

        username = request.POST["username"] #kriege Nutzernamen durch index
        password = request.POST["password"] #kriege Passwort

        if User.objects.filter(
                username=username #wenn nutzername schon existiert
            ).exists():
            
            error = "Benutzername exisitiert bereits" #fehler platzhalter füllen

        else: 

            user = User.objects.create_user( #erstelle nutzer mit username und passwort
                    username=username,
                    password=password
                    )
            login(request,user) #login methode vorgegeben von django

            return redirect("/home/") #weiterleitung zu /home

    return render( #aktuallisiert seite mit fehler
            request,
            "register.html",
            {"error": error})

def login_view(request): #einloggen

    error = "" #fehler platzhalter

    if request.method == "POST": #als POST request
        username = request.POST["username"] #kriege nuternamen durch die index 
        password = request.POST["password"] #kriege passwort durch die index


        user = authenticate(request, #django methode um nutzer mit parametern username und password zu authentizieren
                            username=username,
                            password=password
                            )
        if user: #wenn erfolgreich authentiziert
            login(                #django methode zum einloggen
                    request,
                    user
                    )

            return redirect("/home/") #weiterleitung /home



        error = "Falscher Login" #platzhalter füllung


    return render( #aktualisiere seite mit der fehlermeldung
            request,
            "login.html",
            {
                "error":error
            })

def logout_view(request): #ausloggen
    logout(request) #django methode zum ausloggen

    return redirect("/index/") #weiterleitung index










