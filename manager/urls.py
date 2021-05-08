from django.urls import path
from .views import  HomeView, DashboardView, AirlineList, PilotList, FlightList, PilotDetailView, FlightDetailView,  AirlineDetailView, CabinCrewList, Security
#import views

urlpatterns = [
      #  path('admin/', admin.site.urls),
        path('dashboard/', DashboardView.as_view, name='dashboard'),
        path('airlines/', AirlineList.as_view(), name='airline'),
        path('flights/', FlightList.as_view(), name='flights'),
        path('pilots/', PilotList.as_view(), name='pilots'),
        path('cabin-crew/', CabinCrewList.as_view(), name='cabin-crew'),
        path('security/', Security.as_view(), name='security'),
        path('pilots/<slug:slug>/', PilotDetailView.as_view(), name='pilots-detail'),
        path('flights/<slug:slug>/', FlightDetailView.as_view(), name='flights-detail'),
        path('airlines/<slug:slug>/', AirlineDetailView.as_view(), name='airlines-detail'),
        path('', HomeView.as_view(), name='home'),
]