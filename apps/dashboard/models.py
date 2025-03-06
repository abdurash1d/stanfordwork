from django.db import models
from django.conf import settings

from apps.jobs.models import Job

from config.base_models import BaseModel 


class JobViewLog(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='view_logs')
    viewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='viewed_jobs')
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Job {self.job.title} viewed by {self.viewer.username if self.viewer else 'anonymous'} at {self.viewed_at}"

    class Meta:
        ordering = ['-viewed_at']


class UserActivityLog(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activity_logs')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} performed '{self.action}' at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']


class JobApplicationStats(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='application_stats')
    total_applications = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.total_applications} applications for {self.job.title}"

    class Meta:
        ordering = ['-last_updated']


class AdminDashboardSettings(BaseModel):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return f"{self.key}: {self.value}"

    class Meta:
        ordering = ['key']


class SMSNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SMS Notification to {self.user.username}"
    