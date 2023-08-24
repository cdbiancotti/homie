from django.db import models
from django.core.exceptions import ValidationError
from lkinpractice.myfields import RGBColorField
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


BAD_TITLES = ['test', 'prueba']

def validate_no_bad_words(title):
    if any([title.lower() in BAD_TITLES]):
        raise ValidationError(f"This Post can't has title {title}")    
    
class Lkin(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    text_val = models.CharField(max_length=10, validators=[validate_no_bad_words])
    favorite_color = RGBColorField(null=True)
    born_date = models.DateField(null=True)

    def __str__(self):
        return self.text_val
    
    
class LkinBusiness(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    founded = models.DateField(null=True)
    
    def __str__(self):
        return self.name


class GenericProfile(models.Model):
    content_type = models.ForeignKey(ContentType, null=True,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    subject = GenericForeignKey('content_type', 'object_id')