from django.db import models
from django.utils.timezone import now

from stanfordwork.base_models import BaseModel  


class ContactInfo(BaseModel):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True 


class Company(ContactInfo):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    locations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CompanyResponsiblePerson(ContactInfo):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='responsible_persons')

    def __str__(self):
        return f"{self.full_name} ({self.position})"
