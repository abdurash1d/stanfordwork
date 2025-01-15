from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('candidate', 'Candidate'),
        ('employer', 'Employer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='candidate')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name="users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="users", blank=True)


    class Meta:
        db_table = 'users'


    def __str__(self):
        return f"{self.username} ({self.role})"

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="resume")
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume of {self.user.username}"