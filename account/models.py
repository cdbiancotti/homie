from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)