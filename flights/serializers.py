from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
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
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username,
                        first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserLoginSerializer (serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')
        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)
        data['access'] = token

        try:
            user_obj = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError('This username does not exist')

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError('Incorrect username/password')

        return data
