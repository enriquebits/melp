from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restaurants import views

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurants/<str:pk>/', views.RestaurantDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)