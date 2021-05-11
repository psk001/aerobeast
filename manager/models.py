from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models

import time
from datetime import datetime, timedelta
import pytz


# Create your models here.

class Airline(models.Model):
    airline_id = models.IntegerField( primary_key=True, unique=True)
    airline_name = models.CharField(max_length=100, unique=True)
    airline_emp_count = models.IntegerField()
    airline_flight_count = models.IntegerField()
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.airline_id) + " " + self.airline_name

    def get_absolute_url(self):
        return reverse('airlines-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.airline_name)
        return super().save(*args, **kwargs)
        

class Aircraft(models.Model):
    aircraft_type_choices = [('CARGO', 'Cargo'), ('PASSENGER', 'Passenger'), ('PRIVATE', 'Private')]
    aircraft_id = models.CharField(primary_key=True, unique=True, max_length=100)
    aircraft_name = models.CharField(max_length=100)
    aircraft_type = models.CharField(max_length=20, choices = aircraft_type_choices)
    aircraft_company = models.CharField(max_length=100)
    aircraft_capacity = models.IntegerField()
    aircraft_fuel_capacity = models.IntegerField()
    slug = models.SlugField(null=True, blank=True, max_length=40)


class Pilot(models.Model):
    sex_desig_choices = [('MALE','M'), ('FEMALE','F'),('OTHERS','OTHER'),]
    marital_choices = [('MARRIED', 'Married'), ('UNMARRIED','Unmarried'),]
    pilot_id = models.IntegerField(primary_key=True, unique=True)    
    pilot_name = models.CharField(max_length=100)
    pilot_airline = models.ForeignKey(Airline,
                                     on_delete = models.CASCADE,
                                    )
    pilot_designation = models.CharField(max_length=50)

    pilot_aircraft = models.ForeignKey(Aircraft,
                                      on_delete=models.DO_NOTHING,
                                      )
    pilot_age = models.IntegerField(default=0) 
    pilot_sex = models.CharField(max_length=10, choices=sex_desig_choices , default='not found')
    pilot_marital_status = models.CharField(max_length=10, choices=marital_choices)
    pilot_contact = models.BigIntegerField(null=True, default=0)
    pilot_email = models.EmailField()
    pilot_address = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, max_length=40)

    def __str__(self):
        return str(self.pilot_id) + " " + self.pilot_name

    def get_absolute_url(self):
        return reverse('pilots-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.pilot_name)
        return super().save(*args, **kwargs)


class CrewMembers(models.Model):
    crew_member_id = models.IntegerField(primary_key=True, unique=True)
    crew_member_name = models.CharField(max_length=50 )
    crew_member_airline = models.ForeignKey(Airline,
                                            on_delete=models.CASCADE)
    crew_member_age = models.IntegerField()
    crew_member_contact = models.BigIntegerField()
    slug = models.SlugField(null=True, blank=True, max_length=40)


class GroundStaff(models.Model):
    ground_staff_id = models.IntegerField(primary_key=True, unique=True)
    ground_staff_name = models.CharField(max_length=50 )
    ground_staff_airline = models.ForeignKey(Airline,
                                            on_delete=models.CASCADE)
    ground_staff_age = models.IntegerField()
    ground_staff_contact = models.BigIntegerField()    
    slug = models.SlugField(null=True, blank=True, max_length=40)


class Flight(models.Model):
    flight_id = models.CharField( primary_key=True, unique=True, max_length=20)
    flight_airline = models.ForeignKey(Airline,
                                      on_delete = models.PROTECT,
                                      )
    flight_source = models.CharField(max_length=50)
    flight_destination = models.CharField(max_length=50)
    flight_arrival = models.TimeField(null=True, blank=True)
    flight_departure = models.TimeField(null=True, blank=True)
    flight_delay = models.FloatField()
    flight_gate = models.IntegerField()
    flight_pilot = models.ForeignKey(Pilot,
                                    on_delete = models.CASCADE,
                                    )
    flight_aircraft = models.ForeignKey(Aircraft,
                                        on_delete=models.DO_NOTHING,
                                        )
    flight_crew_members = models.ManyToManyField(CrewMembers)
    flight_ground_staff = models.ManyToManyField(GroundStaff)
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        # try:
        #     ordering = ['flight_arrival']
        # except:
        #     ordering = ['flight_departure']
        # finally:
        pass

    def __str__(self):
        return str(self.flight_id) + "from " + self.flight_source + " to " + self.flight_destination 

    def get_absolute_url(self):
        return reverse('flights-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.flight_id)
        return super().save(*args, **kwargs)

    def time_diff(self):
        curr_time = datetime.now()   #number of seconds since epoch

        # if self.flight_arrival:
        #     timediff = curr_time - self.flight_arrival
        # elif self.flight_departure:
        #     timediff = curr_time - self.flight_departure
         
        return (curr_time)
        

    def get_type(self):
        return self.flight_arrival


class PilotRoster(models.Model):
    job_id = models.IntegerField(primary_key=True, unique=True)
    job_day = models.CharField(max_length=20, null=True, blank=True)
    job_pilot = models.ForeignKey(Pilot, 
                                 on_delete = models.CASCADE)
    job_flight = models.ManyToManyField(Flight)














