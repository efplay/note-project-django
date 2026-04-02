from django.utils import timezone
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField() 
    reminder = models.DateTimeField(null=True, blank=True)  
    created_at = models.DateTimeField(default=timezone.now) 
    
    def add_note(self):
        self.created_at = timezone.now()
        self.save()
        
    def delete_note(self):
        self.created_at = timezone.now() 
        self.delete()
    
    def update_note(self, title, text, reminder):
        if not title:
            raise ValueError("Title cannot be empty.")
        if not text:
            raise ValueError("Text cannot be empty.")
        if len(text) > 1000:
            raise ValueError("Text cannot exceed 1000 characters.")
        self.title = title
        self.text = text
        self.reminder = reminder
        self.created_at = timezone.now()
        self.save() 
        
    def __str__(self):
        return self.title
    

    