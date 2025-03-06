# apps/users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver

def user_post_save(sender, instance, **kwargs):
    # handle signal
    pass
