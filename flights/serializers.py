from rest_framework import serializers
from flights.models import Booking, Flight


class FlightsListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time', 'price']


class BookingListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'flight', 'date']
