from django.db import models
from django.conf import settings
from jobs.models import Job

class JobViewLog(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='view_logs')
    viewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='viewed_jobs')
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Job {self.job.title} viewed by {self.viewer.username if self.viewer else 'anonymous'} at {self.viewed_at}"

    class Meta:
        ordering = ['-viewed_at']


class UserActivityLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activity_logs')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} performed '{self.action}' at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']


class JobApplicationStats(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='application_stats')
    total_applications = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.total_applications} applications for {self.job.title}"

    class Meta:
        ordering = ['-last_updated']


class AdminDashboardSettings(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return f"{self.key}: {self.value}"

    class Meta:
        ordering = ['key']


class JobPostingAnalytics(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='posting_analytics')
    view_count = models.PositiveIntegerField(default=0)
    update_count = models.PositiveIntegerField(default=0)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job {self.job.title} - {self.view_count} views, {self.update_count} updates"

    class Meta:
        ordering = ['-last_updated_at']
