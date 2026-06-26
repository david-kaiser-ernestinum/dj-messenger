from django.shortcuts import render
from chat.models import Chat, Message

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def index_view(request):
    return render(request,"index.html")

@login_required
def home_view(request):
    chats = Chat.objects.filter(members=request.user)
    
    context = {
        "chats": chats
            }

    return render(request, "home.html", context)
    

