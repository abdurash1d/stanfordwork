from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(
        max_length=50,
        choices=[
            ('full-time', 'Full Time'),
            ('part-time', 'Part Time'),
            ('contract', 'Contract')
        ]
    )
    industry = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField()

    def __str__(self):
        return self.title
