from rest_framework import serializers
from flights.models import Flight


class FlightsListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time', 'price']


class BookingListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'flight', 'date']
