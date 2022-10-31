from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.models import Flight
from .serializers import ListSerializer


class FlightListView(ListAPIView):
    # queryset = Flight.objects.all()
    serializer_class = ListSerializer

    def get_queryset(self):
        return Flight.objects.all()
