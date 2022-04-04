from django.http import HttpResponse
from django.shortcuts import render
from .models import Airport

def index(request):
    airports = Airport.objects.all()  # gather data from the database
    context = {'airports': airports}  # assign it to a context variable
    return render(request, 'airports/index.html', context)  # render the template with the context data
def airport_info(request, airport_code):
    airport = Airport.objects.get(airport_code=airport_code)  # gather the data matching the necessary parameters
    context = {'airport': airport}  # attach line 10's result to a context variable
    return render(request, 'airports/airport.html', context)  # render the template using the context variable


