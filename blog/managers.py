from django.db import models

class PostManager(models.Manager):
    def new_to_old(self):
        return self.all().order_by('-date')