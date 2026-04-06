from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', notes_main, name='notes_main'),
    path('notes_list_view/', NoteListView.as_view(), name='view_notes'),
    path('about_site/', about_site, name='about_site'),
    path('notes/create/', NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
