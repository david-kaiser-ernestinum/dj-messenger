from django.shortcuts import get_object_or_404, redirect, render #django methoden für redirect usw.
from django.contrib.auth.decorators import login_required #für login_required
from .models import Chat, Message #datenbank import
from datetime import datetime #zeit biblothek import
from django.http import HttpResponseForbidden #403 import
from django.contrib.auth.models import User #user datenbank import

# Alle Funktonen hier sind nur für angemeldete Benutzer verfügbar

# Erstellen eines Chats
@login_required
def create_chat(request):
    if request.method == "POST":
        name = request.POST.get("name")
        chat=Chat.objects.create(name=name) #Erstellt ein Object Chat
        chat.members.add(request.user) #füge dich selber als Member vom Chat hinzu
    return redirect("home") #weiterleitung home

# Weiterleiten auf die Chatseite, wenn der Nutzer im Chat ist
@login_required
def view_chat(request, chat_id): #Chat angegucken
    chat = get_object_or_404(Chat,id=chat_id) #Variable um Objekt Chat zu speichen

    if not chat.members.filter(id=request.user.id).exists(): #falls User nicht member vom Chat ist
        return HttpResponseForbidden() #403 Nicht erlaubt

    messages = Message.objects.filter(chat=chat).order_by("date") #sortiere Nachrichten nach datum
    context = { #alle messages im chat
        "chat" : chat,
        "messages" : messages
            }
    return render(request,"chat.html", context) #aktuallisiere die seite mit allen nachrichten

# Funktion zum Senden einer Nachricht in einem Chat
@login_required
def send_message(request, chat_id): #Schicke Nachricht
    chat = get_object_or_404(Chat,id=chat_id) #Chat Variable

    if not chat.members.filter(id=request.user.id).exists(): #Falls User nicht member vom Chat ist
        return HttpResponseForbidden() #403 Nicht erlaubt

    if request.method == "POST":
        user = request.user
        content = request.POST.get("content")  
        Message.objects.create( #Neues Message objekt
                chat = chat,  #Infos zur nachricht
                sender = user,
                content = content,
                date = datetime.now()
                )

    return redirect("view_chat", chat_id)#aktuallisiere seite mit der neuen nachricht

# Funktion für das Hinzufügen von Nutzern zu einem Chat
@login_required
def add_user(request, chat_id): #Nutzer hinzufügen
    chat = get_object_or_404(Chat,id=chat_id) #Object Speichern oder 404

    if not chat.members.filter(id=request.user.id).exists(): 
        return HttpResponseForbidden() # 403

    if request.method == "POST": #Schicke als POST request
        username = request.POST.get("username") #Kriege den username aus der POST

        try: #Versuche
            new_user = User.objects.get(username=username) #Neuen nutzer aus mit Username speichern
            chat.members.add(new_user) #füge neuen Benuzter hinzu
        except User.DoesNotExist: #Falls User nicht existiert
            pass #nichts
        
    return redirect("view_chat", chat_id) #weiterleitung zum neuen chat

