from django.contrib import admin

from notes.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'reminder')
    search_fields = ('title', 'text')
    
    
admin.site.register(Note, NoteAdmin)