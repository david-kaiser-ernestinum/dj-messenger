from django.db import models 
from django.contrib.auth.models import User


# Datenbankobjekt für die Chats:
class Chat(models.Model):
    name = models.CharField(max_length=30)

    # Hiermit wird die Zwischentabelle ersetzt
    members = models.ManyToManyField(User)

    # Diese Funktion sorgt dafür, dass der Name des Chats im Admin-Interface eingesehen werden kann
    def __str__(self): 
        return self.name

# Datenbankobjekt für die Nachrichten 
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    date = models.DateField()

