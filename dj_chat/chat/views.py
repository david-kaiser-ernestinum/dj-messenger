from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Chat
# Create your views here.

@login_required
def create_chat(request):
    if request.method == "POST":
        name = request.POST.get("name")
        chat=Chat.objects.create(name=name)
        chat.members.add(request.user) 
    return redirect("home")

