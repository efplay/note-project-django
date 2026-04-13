from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']