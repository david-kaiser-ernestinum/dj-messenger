from django.db import models 
from django.contrib.auth.models import User
# Create your models here.
# Datenbankstruktur Chat

class Chat(models.Model): #Chat Table
    name = models.CharField(max_length=30) #Name mit maximaler länge von 30 chars
    #ersetzt die Zwischentabelle 
    members = models.ManyToManyField(User) # 

    def __str__(self): 
        return self.name 


class Message(models.Model): #Message Table
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE) #klaut von Chat
    sender = models.ForeignKey(User, on_delete=models.CASCADE) #sender klaut user von User
    content = models.CharField(max_length=1000) #nachricht mit 1000 Zeichen
    date = models.DateField() #Datum
# CASCADE löscht feld wenn ForeignKey gelöscht wird

