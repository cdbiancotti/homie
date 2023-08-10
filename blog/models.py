from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Publicacion(models.Model):
    
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=60)
    cuerpo = RichTextField(blank=True, null=True)
    autor = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog', blank=True, null=True)
    
    def __str__(self):
        return f'{self.titulo} ({self.autor})'
