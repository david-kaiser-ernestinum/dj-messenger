from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from datetime import datetime
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

# Create your views here.

@login_required #Abschntitt, damit Methode nur mit Account funktioniert
def create_chat(request): #Neue Chat erstellen
    if request.method == "POST": #Schicke als POST request
        name = request.POST.get("name")
        chat=Chat.objects.create(name=name) #Erstellt ein Object Chat
        chat.members.add(request.user) #füge dich selber als Member vom Chat hinzu
    return redirect("home") #weiterleitung home

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
    return render(request,"chat.html", context) 


@login_required
def send_message(request, chat_id): #Schicke Nachricht
    chat = get_object_or_404(Chat,id=chat_id) #Chat Variable

    if not chat.members.filter(id=request.user.id).exists(): #Falls User nicht member vom Chat ist
        return HttpResponseForbidden() #403 Nicht erlaubt



    if request.method == "POST": #Schicke als POST request
        user = request.user #User speichern
        content = request.POST.get("content")  
        Message.objects.create( #Neues Message objekt
                chat = chat,  #Infos zur nachricht
                sender = user,
                content = content,
                date = datetime.now()
                )

    return redirect("view_chat", chat_id)

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

