
from django.contrib import admin
from .models import  Aircraft, Airline, Pilot, Flight, PilotRoster, CrewMembers, GroundStaff


userModels = [ Aircraft, Airline, Pilot, Flight, PilotRoster, CrewMembers, GroundStaff]
admin.site.register(userModels)

