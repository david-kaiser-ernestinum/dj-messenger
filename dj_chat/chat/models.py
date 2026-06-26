from django.db import models 
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=30)
    #ersetzt die Zwischentabelle 
    members = models.ManyToManyField(User)

    def __str__(self): 
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    date = models.DateField()

