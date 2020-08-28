from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restaurants import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('restaurants/',
        views.RestaurantList.as_view(),
        name='restaurant-list'),
    path('restaurants/statistics/',
        views.RestaurantStatistics.as_view(),
        name='restaurant-statistics'),
    path('restaurants/<str:pk>/',
        views.RestaurantDetail.as_view(),
        name='restaurant-detail'),
])

