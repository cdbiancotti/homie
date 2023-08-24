from rest_framework.viewsets import ModelViewSet
from qchat.models import Message
from qchat.serializers import MessageSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer