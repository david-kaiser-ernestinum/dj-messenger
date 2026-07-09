from django.urls import path
from .views import create_chat, view_chat, send_message, add_user

# Alle URLs für die Chatfunktion
urlpatterns = [
    # Die seite für die Chats
    path("<int:chat_id>/", view_chat, name="view_chat"),
    
    # Die APIs für die Funktionen (erstellen, hinzufügen, senden)
    path("create/", create_chat, name="create_chat"),
    path("send_message/<int:chat_id>/", send_message, name="send_message"),
    path("add_user/<int:chat_id>/", add_user, name="add_user"),
]

