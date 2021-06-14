from django.shortcuts import render
from flightApp.models import Flight, Passenger, Resarvation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ResarvationSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],
                                   arrivalCity=request.data['arrivalCity'],
                                   dateOfDeparture=request.data['dateOfDeparture'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightID'])
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()
    
    reservation = Resarvation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ResarvationViewSet(viewsets.ModelViewSet):
    queryset = Resarvation.objects.all()
    serializer_class = ResarvationSerializer
