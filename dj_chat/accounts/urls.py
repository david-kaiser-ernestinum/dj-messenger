from django.urls import path #importiere die projekt urls.py

from .views import register_view #importiere views.py methoden
from .views import login_view
from .views import logout_view

urlpatterns = [
        path("register/",        #register seite
             register_view,
             name="register",
        ),
        
        path("login/",           #login seite
             login_view,
             name="login",
        ),

        path("logout/",          #logout seite, die wieder auf /index.html weiterleitet
             logout_view,
             name="logout",
        ),
        ]
