from django.shortcuts import render
from chat.models import Chat, Message

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

# Weiterleitung zur Startseite
def index_view(request):
    return render(request,"index.html")

# Auf der Home-Seite werden alle Chats angezeigt
@login_required
def home_view(request):
    chats = Chat.objects.filter(members=request.user)

    playsound = False
    if request.GET.get("sound"):
        playsound = request.GET.get("sound")

    
    context = {
        "chats": chats,
        "play_sound": playsound
            }

    return render(request, "home.html", context)
    

