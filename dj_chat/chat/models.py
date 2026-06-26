from django.db import models 
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=30)

class is_member(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    member_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    date = models.DateField()
