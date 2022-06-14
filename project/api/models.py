from django.db import models


# Create your models here.

class Blood_Bank(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
