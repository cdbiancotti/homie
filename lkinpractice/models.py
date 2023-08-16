from django.db import models
from django.core.exceptions import ValidationError
from lkinpractice.myfields import RGBColorField

BAD_TITLES = ['test', 'prueba']

def validate_no_bad_words(title):
    if any([title.lower() in BAD_TITLES]):
        raise ValidationError(f"This Post can't has title {title}")    
    
class Lkin(models.Model):
    text_val = models.CharField(max_length=10, validators=[validate_no_bad_words])
    favorite_color = RGBColorField(null=True)