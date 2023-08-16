from django.db import models
from ckeditor.fields import RichTextField 
    
class Publicacion(models.Model):
    
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=60)
    body = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} ({self.author})'
