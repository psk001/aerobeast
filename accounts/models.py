from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser
from manager.models import Pilot, CrewMembers, GroundStaff
#from rolepermissions.roles import AbstractUserRole


from django.db import models

class CustomUser(AbstractUser):
    role_choices = (
                     ('ATC','ATC'), 
                     ('ADMIN','Admin'),
                     ('PILOT','Pilot'), 
                     ('CABIN_CREW','Cabin Crew'), 
                     ('GROUND STAFF','Ground Staff'),
                    )
    user_designation = models.CharField(max_length=20, choices =role_choices)

class PilotUser(models.Model):
    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE )

    class Meta:
        permissions = [
            ('view_pilot_detail', 'can view the pilot detail page'),
            ('view_airline_detail', 'can view the airline detail page'),
        ]

class AtcUser(models.Model):
    user = models.OneToOneField(CustomUser,   
                                on_delete = models.CASCADE)

    class Meta:
        permissions = [
            ('view_flight_detail', 'can view the flight detail page'),
             ('view_airline_detail', 'can view the airline detail page'),
        ]


