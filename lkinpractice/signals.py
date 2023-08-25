from django.dispatch import receiver
from django.db.models.signals import post_save
from lkinpractice.models import Lkin, LkinBusiness, GenericProfile

@receiver(post_save, sender=Lkin)
def create_profile_lkin(instance, created, **kwargs):
    if created:
        GenericProfile.objects.create(subject=instance)

@receiver(post_save, sender=LkinBusiness)
def create_profile_lkinbusiness(instance, created, **kwargs):
    if created:
        GenericProfile.objects.create(subject=instance)


