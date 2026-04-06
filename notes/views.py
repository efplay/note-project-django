from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django import forms
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect

from notes.models import Note


def notes_main(request):
    return render(request, 'notes.html')

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})
    
def about_site(request):
    return render(request, 'about_site.html')
