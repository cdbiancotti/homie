from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('pages/create', views.PublicacionCreateView.as_view(), name='create_page'),
    path('pages/<int:pk>', views.PublicacionDetailView.as_view(), name='details_page'),
    path('pages/<int:pk>/update', views.PublicacionUpdateView.as_view(), name='update_page'),
    path('pages/<int:pk>/delete', views.PublicacionDeleteView.as_view(), name='delete_page'),
]
