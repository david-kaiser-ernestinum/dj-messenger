from django.urls import path  

# importieren der views-Methoden
from .views import index_view 
from .views import home_view

# Alle Seiten für die Startseite und die Home-Seite
urlpatterns = [
        path("",
             index_view,
             name="index",
        ),
        
        path("index/",          
             index_view,
             name="index",
        ),

        path("home/",          
             home_view,
             name="home",
        ),

        ]
