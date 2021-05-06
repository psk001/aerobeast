
from django.contrib import admin
from .models import  Aircraft, Airline, Pilot, Flight, PilotRoster

# Register your models here.

userModels = [ Aircraft, Airline, Pilot, Flight, PilotRoster]
admin.site.register(userModels)

