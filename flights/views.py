from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import FlightsListSerializer, BookingListSerializer
from datetime import datetime


class FlightListView(ListAPIView):
    # queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

    def get_queryset(self):
        return Flight.objects.all()


class BookingsListView (ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer
