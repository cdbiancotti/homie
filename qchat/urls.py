from django.urls import path, include
from rest_framework.routers import DefaultRouter
from qchat.views import MessageViewSet

message_router = DefaultRouter()
message_router.register(r'messages', MessageViewSet)

# router = DefaultRouter()
# qchat
# router.registry.extend(message_router.registry)

urlpatterns = [
    path('', include(message_router.urls))
]



