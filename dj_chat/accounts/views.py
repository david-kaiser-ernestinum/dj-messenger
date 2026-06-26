from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

def register_view(request):

    error = ""

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(
                username=username
            ).exists():
            
            error = "Benutzername exisitiert bereits"

        else: 

            user = User.objects.create_user(
                    username=username,
                    password=password
                    )
            login(request,user)

            return redirect("/home/")

    return render(
            request,
            "register.html",
            {"error": error})

def login_view(request):

    error = ""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]


        user = authenticate(request,
                            username=username,
                            password=password
                            )
        if user:
            login(
                    request,
                    user
                    )

            return redirect("/home/")



        error = "Falscher Login"


    return render(
            request,
            "login.html",
            {
                "error":error
            })

def logout_view(request):
    logout(request)

    return redirect("/index/")










