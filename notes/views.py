

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib import messages
from notes.models import Note
from django.urls import reverse_lazy
from .forms import NoteForm, LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout


def notes_main(request):
    return render(request, 'notes.html')


    
def about_site(request):
    return render(request, 'about_site.html')


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('view_notes')


class NoteListView(ListView):
    model = Note
    template_name = 'view_notes.html'
    context_object_name = 'notes'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset
    
class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'
    

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('view_notes')
    
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('view_notes')

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Successfully {username} logged in!")
                return redirect('notes_main')
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}!")
            return redirect('notes_main')
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('notes_main')