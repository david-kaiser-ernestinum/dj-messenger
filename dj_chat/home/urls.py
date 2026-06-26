from django.urls import path

from .views import index_view
from .views import home_view

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
