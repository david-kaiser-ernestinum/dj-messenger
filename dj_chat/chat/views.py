from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from datetime import datetime
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

# Alle Funktonen hier sind nur für angemeldete Benutzer verfügbar

# Erstellen eines Chats
@login_required
def create_chat(request):
    if request.method == "POST":
        name = request.POST.get("name")
        chat=Chat.objects.create(name=name)
        chat.members.add(request.user) 
    return redirect("home")

# Weiterleiten auf die Chatseite, wenn der Nutzer im Chat ist
@login_required
def view_chat(request, chat_id):
    chat = get_object_or_404(Chat,id=chat_id)

    if not chat.members.filter(id=request.user.id).exists():
        return HttpResponseForbidden()

    messages = Message.objects.filter(chat=chat).order_by("date")        
    context = {
        "chat" : chat,
        "messages" : messages
            }
    return render(request,"chat.html", context)

# Funktion zum Senden einer Nachricht in einem Chat
@login_required
def send_message(request, chat_id):
    chat = get_object_or_404(Chat,id=chat_id)

    if not chat.members.filter(id=request.user.id).exists():
        return HttpResponseForbidden()

    if request.method == "POST":
        user = request.user
        content = request.POST.get("content")  
        Message.objects.create(
                chat = chat,
                sender = user,
                content = content,
                date = datetime.now()
                )

    return redirect("view_chat", chat_id)

# Funktion für das Hinzufügen von Nutzern zu einem Chat
@login_required
def add_user(request, chat_id):
    chat = get_object_or_404(Chat,id=chat_id)

    if not chat.members.filter(id=request.user.id).exists():
        return HttpResponseForbidden()

    if request.method == "POST":
        username = request.POST.get("username")

        try:
            new_user = User.objects.get(username=username)
            chat.members.add(new_user)
        except User.DoesNotExist:
            pass
        
    return redirect("view_chat", chat_id)

