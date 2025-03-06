from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from apps.dashboard.models import SMSNotification

@receiver(post_save, sender=SMSNotification)
def send_notification_email(sender, instance, **kwargs):
    send_mail(
        'New SMS Notification',
        instance.message,
        'no-reply@timepartner.com',
        [instance.user.email],
        fail_silently=False,
    )
    