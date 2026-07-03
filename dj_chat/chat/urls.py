from django.urls import path
from .views import create_chat, view_chat, send_message, add_user

urlpatterns = [
    path("create/", create_chat, name="create_chat"), #URL-Pfad um ein Chat zu erstellen
    path("<int:chat_id>/", view_chat, name="view_chat"), #URL-Pfad um den Chat zu sehen
    path("send_message/<int:chat_id>/", send_message, name="send_message"), #URL-Pfad um eine Nachricht zu schicken
    path("add_user/<int:chat_id>/", add_user, name="add_user"), #URL-Pfad um einen neuen Teilnehmer hinzuzufügen
]

