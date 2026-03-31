from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django import forms
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect


def notes_main(request):
    return render(request, 'notes.html')
    
