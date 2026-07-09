from django.contrib import admin
from .models import Chat,Message

# Hier werden unsere eigenen Datenbankobjekte für das Admin-Interface sichtbar gemacht
admin.site.register(Chat)
admin.site.register(Message)
