from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}
        

class MyUserUpdateForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput, required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    avatar = forms.ImageField()
    descripcion = forms.CharField(widget=CKEditorWidget())
    link = forms.URLField()