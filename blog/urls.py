from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pages/', views.PostListView.as_view(), name='pages'),
    path('pages/create', views.PostCreateView.as_view(), name='create_page'),
    path('pages/<int:pk>', views.PostDetailView.as_view(), name='details_page'),
    path('pages/<int:pk>/update', views.PostUpdateView.as_view(), name='update_page'),
    path('pages/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete_page'),
]
