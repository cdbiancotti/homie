from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError

BAD_TITLES = ['test', 'prueba']

def validate_no_bad_words(title):
    if any([title.lower() in BAD_TITLES]):
        raise ValidationError(f"This Post can't has title {title}")    
    
class Publicacion(models.Model):
    
    title = models.CharField(max_length=40, validators=[validate_no_bad_words])
    subtitle = models.CharField(max_length=60)
    body = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} ({self.author})'
