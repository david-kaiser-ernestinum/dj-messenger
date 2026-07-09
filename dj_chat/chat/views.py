from django.shortcuts import get_object_or_404, redirect, render 
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
        eastereggs = ["luracks", "michael", "falk", "jacob", "jonathan", "raphael"]
        if name in eastereggs:
            return redirect(f"{reverse("home")}?sound={name}")

    return redirect("home") 

# Weiterleiten auf die Chatseite, wenn der Nutzer im Chat ist
@login_required
def view_chat(request, chat_id): 
    chat = get_object_or_404(Chat,id=chat_id) 

    # Mitglierder die nicht im Chat sind bekommen keinen Zugriff
    if not chat.members.filter(id=request.user.id).exists(): 
        return HttpResponseForbidden() 
    
    # Alle Nachricht im Chat nach Datum sortiert ausgeben
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

    # Mitglierder die nicht im Chat sind bekommen keinen Zugriff
    if not chat.members.filter(id=request.user.id).exists(): 
        return HttpResponseForbidden() 
    
    # Beim senden eine Nachricht erstellen
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

    # Mitglierder die nicht im Chat sind bekommen keinen Zugriff
    if not chat.members.filter(id=request.user.id).exists(): 
        return HttpResponseForbidden() # 403

    if request.method == "POST": 
        username = request.POST.get("username") 

        # Testen ob es den Nutzer gibt
        try: 
            new_user = User.objects.get(username=username) 
            chat.members.add(new_user) 
        except User.DoesNotExist:
            pass 
        
    return redirect("view_chat", chat_id) 

