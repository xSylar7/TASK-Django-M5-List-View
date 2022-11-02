from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import BookingDetailSerializer, FlightsListSerializer, BookingListSerializer, BookingUpdateSerializer
from datetime import datetime


class FlightListView(ListAPIView):
    # queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

    def get_queryset(self):
        return Flight.objects.all()


class BookingsListView (ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer


class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
