from django.db import models


class Message(models.Model):
    header = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return f'Message header: {self.header}'
    