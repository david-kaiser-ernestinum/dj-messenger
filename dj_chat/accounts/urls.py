from django.urls import path 

# importieren der views-Methoden
from .views import register_view 
from .views import login_view
from .views import logout_view

# Alle Seiten die mit Accounts zu tun haben:
urlpatterns = [
        # zum Registrieren
        path("register/",
             register_view,
             name="register",
        ),
        
        # zum Anmelden
        path("login/",
             login_view,
             name="login",
        ),
        
        # zum Abmelden
        path("logout/",          
             logout_view,
             name="logout",
        ),]
