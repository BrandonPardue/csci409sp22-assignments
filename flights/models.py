from django.db import models
from airports.models import Airport
# Create your models here.

class Airline(models.Model):
    airline_name = models.CharField(max_length=30)
    airline_code = models.CharField(max_length=2)

    def __str__(self):
        return self.airline_code



class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='flight_origin')
    destination = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='flight_destination')
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    aircraft_type = models.CharField(max_length=10)
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT, related_name='flight_airline')
    flight_number = models.IntegerField()

    def __str__(self):
        return self.airline.airline_code + str(self.flight_number)



