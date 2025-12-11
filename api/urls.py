from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.get_locations),
    path('recommend/', views.recommend_trip),
]