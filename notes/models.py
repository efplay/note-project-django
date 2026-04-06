from django.urls import reverse
from django.utils import timezone
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField() 
    reminder = models.DateTimeField(null=True, blank=True)  
    created_at = models.DateTimeField(default=timezone.now) 
        
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title', 'created_at']
        
    def get_absolute_url(self):
        return reverse('note-detail', kwargs={"pk": self.pk})
    
    

    