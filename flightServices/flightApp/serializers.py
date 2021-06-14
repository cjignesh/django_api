from rest_framework import serializers
from flightApp.models import Flight, Passenger, Resarvation

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ResarvationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resarvation
        fields = '__all__'
