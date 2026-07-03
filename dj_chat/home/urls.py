from django.urls import path  #importiere die project urls.py

from .views import index_view #importiere die views
from .views import home_view

urlpatterns = [
        path("",                #wenn seite ohne pfad aufgerufen wird wird index angezeigt
             index_view,
             name="index",
        ),
        
        path("index/",          #index pfad
             index_view,
             name="index",
        ),

        path("home/",          #homepage pfad
             home_view,
             name="home",
        ),

        ]
