from django.urls import path
from .views import create_chat, view_chat, send_message, add_user

urlpatterns = [
    path("create/", create_chat, name="create_chat"),
    path("<int:chat_id>/", view_chat, name="view_chat"),
    path("send_message/<int:chat_id>/", send_message, name="send_message"),
    path("add_user/<int:chat_id>/", add_user, name="add_user"),
]

