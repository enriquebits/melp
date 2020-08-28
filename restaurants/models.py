import uuid
from django.db import models

# Create your models here.

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.SmallIntegerField()
    name = models.CharField(max_length=128, blank=False)
    site = models.URLField()
    email = models.CharField(max_length=128, blank=True, default='')
    phone = models.CharField(max_length=32, blank=True, default='')
    street = models.CharField(max_length=128, blank=True, default='')
    city = models.CharField(max_length=128, blank=True, default='')
    state = models.CharField(max_length=128, blank=True, default='')
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        ordering = ['name']