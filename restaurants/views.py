import math
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from django.db.models import Avg, StdDev



@api_view(['GET'])
def api_root(request):
    return Response({
        'restaurants': reverse('restaurant-list', request=request)
    })

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantStatistics(APIView):
    """
    List of restaurants that fall inside the circle with center [x,y] y radius z
    """

    def get(self, request):
        restaurants = Restaurant.objects.filter(
            location__distance_lt=(
                Point(float(request.query_params.get("longitude")),
                      float(request.query_params.get("latitude"))),
                Distance(m=request.query_params.get("radius"))))
        count = len(restaurants)
        agg = restaurants.aggregate(avg=Avg('rating'), std=StdDev('rating'))

        return Response({
            "count": count,
            "avg": math.floor(agg["avg"]),
            "std": agg["std"]
        })
