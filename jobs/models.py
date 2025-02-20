from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

from stanfordwork.base_models import BaseModel

class JobCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Job(BaseModel):
    JOB_TYPE_CHOICES = [
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('contract', 'Contract'),
    ]
    TIMELY_TYPE_CHOICES = [
        ('morning', 'Morning'),
        ('night', 'Night'),
        ('flexible', 'Flexible')
    ]
    GENDER_CHOICES = [
        ('Any', 'Any'),
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    
    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='jobs', default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES, default='full-time')
    company = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    application_deadline = models.DateTimeField(null=True, blank=True)
    quota = models.IntegerField(null=True, blank=True)
    perks = models.TextField(null=True, blank=True)
    tasks = models.TextField(null=True, blank=True)
    qualifications = models.TextField(null=True, blank=True)
    timely_type = models.CharField(max_length=50, choices=TIMELY_TYPE_CHOICES, default='morning')
    gender_requirement = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Any')
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='jobs', default=1)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title


class JobInquiry(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='inquiries',null=True,        # Allow null values temporarily
        blank=True )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inquiry for {self.job.title} by {self.name}'


class Application(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('applied', 'Applied'),
        ('under_review', 'Under Review'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='applied')
    
    class Meta:
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title} ({self.status})"
    

class Review(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username}"


class UploadedFile(BaseModel):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
