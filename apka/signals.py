from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save

@receiver(post_save, sender = User)
def profile_after_user_create(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile(user = instance, username = instance.username)
        profile.save()

@receiver(post_save, sender=Invitation)
def print_only_after_deal_created(sender, instance, created, **kwargs):
    if instance.accepted == True:
        instance.delete()
        friend_1 = Friendship(user = instance.from_som, friend = instance.to_som)
        friend_2 = Friendship(user = instance.to_som , friend = instance.from_som)
        friend_1.save(), friend_2.save()