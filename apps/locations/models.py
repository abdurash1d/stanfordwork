from django.db import models
from config.base_models import BaseModel


class Location(BaseModel):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.city}, {self.country}"
