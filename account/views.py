from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

from account.models import MyUser
from .forms import MyUserCreationForm, MyUserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def login_request(request):
    
    if request.method == 'POST':
        auth_form = AuthenticationForm(request, data = request.POST)
    
        if auth_form.is_valid():
            username = auth_form.cleaned_data.get('username')
            password = auth_form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                return render(request, 'blog/index.html', {'msg': 'Te has logueado con exito!'})        
            else:
                return render(request, 'account/login.html', {'form': auth_form, 'error_msg': 'datos incorrectos'})        
        else:
            return render(request, 'account/login.html', {'form': auth_form, 'error_msg': 'formulario incorrecto'})
    
    form = AuthenticationForm()
    
    return render(request, 'account/login.html', {'form': form})

def signup(request):           
         
    if request.method == 'POST':
        user_creation_form = MyUserCreationForm(request.POST)
    
        if user_creation_form.is_valid():
            username = user_creation_form.cleaned_data.get('username')
            user_creation_form.save()
            return render(request, 'blog/index.html', {'msg': f'Se creo el usuario {username}.'})        
        else:
            return render(request, 'account/signup.html', {'form': user_creation_form, 'error_msg': 'datos incorrectos'}) 
            
    user_creation_form = MyUserCreationForm()
    
    return render(request, 'account/signup.html', {'form': user_creation_form, 'error_msg': ''})        

@login_required
def profile(request):
    my_user, _ = MyUser.objects.get_or_create(user=request.user)
    return render(request, 'account/profile.html', {'my_user': my_user})        

@login_required
def update_profile(request):
    my_user, _ = MyUser.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_update_form = MyUserUpdateForm(request.POST, request.FILES)
    
        if user_update_form.is_valid():
            data = user_update_form.cleaned_data
            
            request.user.first_name = data['first_name']
            request.user.last_name = data['last_name']
            request.user.email = data['email']
            if data['password1'] != '' and data['password1'] == data['password2']:
                request.user.set_password(data['password1'])
            
            my_user.avatar = data['avatar']
            my_user.link = data['link']
            my_user.descripcion = data['descripcion']
            
            request.user.save()
            my_user.save()
            return render(request, 'account/profile.html', {'my_user': my_user})        
        else:
            return render(request, 'account/update_profile.html', {'data_form': user_update_form, 'error_msg': 'datos incorrectos'}) 
            
    user_update_form = MyUserUpdateForm(
        initial= {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'password1': '',
            'password2': '',
            'email': request.user.email,
            'avatar': my_user.avatar,
            'descripcion': my_user.descripcion,
            'link': my_user.link
        }
    )
    
    return render(request, 'account/update_profile.html', {'data_form': user_update_form, 'error_msg': ''})