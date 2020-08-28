import uuid
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


# Create your models here.

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    rating = models.SmallIntegerField()
    name = models.CharField(max_length=128, blank=False)
    site = models.URLField()
    email = models.CharField(max_length=128, blank=True, default='')
    phone = models.CharField(max_length=32, blank=True, default='')
    street = models.CharField(max_length=128, blank=True, default='')
    city = models.CharField(max_length=128, blank=True, default='')
    state = models.CharField(max_length=128, blank=True, default='')
    location = models.PointField(geography=True, default=Point(0.0, 0.0))
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        ordering = ['name']
