
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from notes.models import Note
from django.urls import reverse_lazy
from .forms import NoteForm
from datetime import timedelta
from datetime import datetime

def notes_main(request):
    return render(request, 'notes.html')

# def notes_list(request):
#     notes = Note.objects.all()
#     title = request.GET.get('title')
#     if title:
#         notes = notes.filter(title__icontains=title)
#     return render(request, 'view_notes.html', {'notes': notes})
    
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
    