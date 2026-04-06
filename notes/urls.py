from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', notes_main, name='notes_main'),
    path('notes_list/', notes_list, name='notes_list'),
    path('about_site/', about_site, name='about_site'),
]
