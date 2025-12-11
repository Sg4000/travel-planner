from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
import random
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Trip
from .serializers import TripSerializer

@api_view(['GET'])
def get_locations(request):
    locations = Location.objects.all()
    
    serializer = LocationSerializer(locations, many=True)
    
    return Response(serializer.data)



@api_view(['GET', 'POST']) 
def recommend_trip(request):
    if request.method == 'GET':
        return Response({"message": "Send me a POST request with your budget!"})

    if request.method == 'POST':
        user_budget = request.data.get('budget')
        user_category = request.data.get('category')

        matches = Location.objects.all()

        if user_budget:
            matches = matches.filter(cost__lte=user_budget)
        
        if user_category:
            matches = matches.filter(category__iexact=user_category)

        serializer = LocationSerializer(matches, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) 
def manage_trips(request):
    if request.method == 'GET':
        my_trips = Trip.objects.filter(user=request.user)
        serializer = TripSerializer(my_trips, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        location_ids = request.data.get('location_ids')
        
        new_trip = Trip.objects.create(user=request.user)
        
        if location_ids:
            new_trip.locations.set(location_ids)
        
        new_trip.save()
        return Response({"message": "Trip Saved Successfully!", "trip_id": new_trip.id})