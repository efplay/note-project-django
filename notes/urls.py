from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', notes_main, name='notes_main'),
    
]
