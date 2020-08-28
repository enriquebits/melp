from django.db import models

# Create your models here.

class Restaurant(models.Model):
    rating = models.SmallIntegerField()
    name = models.CharField(max_length=128, blank=False)
    site = models.TextField()
    email = models.CharField(max_length=128, blank=True, default='')
    phone = models.CharField(max_length=32, blank=True, default='')
    street = models.CharField(max_length=128, blank=True, default='')
    city = models.CharField(max_length=128, blank=True, default='')
    state = models.CharField(max_length=128, blank=True, default='')
    lat = models.FloatField(min_value=-90, max_value=90)
    lng = models.FloatField(min_value=-180, max_value=180)

    class Meta:
        ordering = ['created']