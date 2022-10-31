from rest_framework import serializers
from flights.models import Flight


class ListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time', 'price']
