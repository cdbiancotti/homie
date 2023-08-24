"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')),
    path('lkin/', include('lkinpractice.urls')),
    path('qchat/', include('qchat.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
