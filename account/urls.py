from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]
