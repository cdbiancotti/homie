from django.urls import path
from lkinpractice import views

app_name= 'lkin'

urlpatterns = [
    path('', views.LkinView.as_view(), name='lkin'),
    path('profile/<int:pk>', views.LkinProfile.as_view(), name='lkin_profile')
]
