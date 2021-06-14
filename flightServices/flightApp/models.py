from django.db import models

# Create your models here.

class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingArlines = models.CharField(max_length=10)
    departureCity = models.CharField(max_length=10)
    arrivalCity = models.CharField(max_length=10)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()
    def __str__(self):
        return self.flightNumber

class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Resarvation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

