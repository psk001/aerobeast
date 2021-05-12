from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Aircraft, Airline, Pilot, Flight, CrewMembers, GroundStaff, PilotRoster
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

class HomeView(ListView):
    model = Flight
    template_name = 'homepage.html'      

    class Meta:
        try:
            ordering = ['flight_arrival']
        except:
            ordering = ['flight_departure']
        finally:
            ordering = ['flight_id']

class AirlineList(ListView):
    model = Airline
    template_name = 'airline_list.html'
    context_object_name = 'airline_list' 


class PilotList(LoginRequiredMixin, ListView):
    model = Pilot
    template_name = 'pilot_list.html'
    context_object_name = 'pilot_list'


class PilotDetailView(LoginRequiredMixin, DetailView):
    model = Pilot
    template_name = 'pilot_detail.html'
    context_object_name = 'pilot_list'


class PilotSortedView(LoginRequiredMixin, ListView):
    model = Pilot
    template_name = 'pilot_detail.html'
    context_object_name = 'pilot_list'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'pilot_age')
        # validate ordering here
        if True:
            return ordering   


class FlightList(ListView):
    model = Flight  
    template_name = 'flight_list.html' 
    context_object_name = 'flight_list'


class FlightDetailView(LoginRequiredMixin, DetailView):
    model = Flight
    template_name = 'flight_detail.html'
    context_object_name = 'flight_list'


class AirlineDetailView(DetailView):
    model = Airline
    template_name = 'airline_detail.html'


class Security(LoginRequiredMixin, ListView):
    model = GroundStaff
    template_name = 'ground_staff_list.html'
    context_object_name = 'ground_staff_list'


class CabinCrewList(LoginRequiredMixin, ListView):
    model = CrewMembers
    template_name = 'cabin_crew_list.html'
    context_object_name = 'cabin_crew_list'


class SearchView(ListView):
    model = Flight
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    #def get_queryset(self):
    #    result = super(SearchView, self).get_queryset()
    #    query = self.request.GET.get('search')
    #    if query:
    #       postresult = Flight.objects.filter(title__contains=query)
    #       result = postresult
    #    else:
    #        result = None
    #    return result


class AircraftList(ListView):
    model=Aircraft
    template_name='aircraft_list.html'
    context_object_name = 'aircraft_list'


def DashboardView(request):
    return render(request, 'dashboard.html')
    
