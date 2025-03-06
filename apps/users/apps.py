# apps/users/apps.py
from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self):
        from . import signals  # import signals module
        User = get_user_model()
        post_save.connect(signals.user_post_save, sender=User)
