from rest_framework import serializers
from restaurants.models import Restaurant


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state',
                  'lat', 'lng']