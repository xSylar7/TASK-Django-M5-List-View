from rest_framework import serializers
from flights.models import Booking, Flight
from django.contrib.auth.models import User


class FlightsListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time', 'price']


class BookingListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'flight', 'date']


class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'flight', 'date', 'passengers']


class BookingUpdateSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['date', 'passengers']


class UserCreateSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create_user(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data
