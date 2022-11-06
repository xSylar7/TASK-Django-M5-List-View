from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import BookingDetailSerializer, FlightsListSerializer, BookingListSerializer, BookingUpdateSerializer, UserCreateSerializer, UserLoginSerializer
from datetime import datetime


class FlightListView(ListAPIView):
    # queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Flight.objects.all()


class BookingsListView (ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated]


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


class BookingCancel (DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class BookFlight (CreateAPIView):
    serializer_class = BookingUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        Flight_id=self.kwargs['flight_id'])

    permission_classes = [IsAuthenticated]


class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class UserCreateView (CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated]


class UserLoginView (APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
