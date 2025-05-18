from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import VolunteerProfile

@receiver(post_save, sender=User)
def create_volunteer_profile(sender, instance, created, **kwargs):
    if created:
        VolunteerProfile.objects.create(user=instance)
