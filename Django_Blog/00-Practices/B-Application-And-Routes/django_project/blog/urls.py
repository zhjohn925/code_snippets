# This is blog urls

from django.urls import path
from . import views

# home() page rounte
urlpatterns = [
    #The empty('') path is mapped to home() in views.py
    path('', views.home, name='blog-home'),   
    #The ('about/') path is mapped to about() in views.py
    path('about/', views.about, name='blog-about'),     
]