from django.db import models

from stanfordwork.base_models import BaseModel
# from django.conf import settings
from jobs.models import Job


class JobPostingAnalytics(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='posting_analytics')
    view_count = models.PositiveIntegerField(default=0)
    update_count = models.PositiveIntegerField(default=0)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job {self.job.title} - {self.view_count} views, {self.update_count} updates"

    class Meta:
        ordering = ['-last_updated_at']
