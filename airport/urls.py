"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from flights.views import FlightListView, BookingsListView, BookingDetailView, BookingUpdateView, BookingDeleteView, UserCreateView, UserLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flight/", FlightListView.as_view(), name='flights-list'),
    path("booking/", BookingsListView.as_view(), name='booking-list'),
    path("detail/<int:booking_id>/",
         BookingDetailView.as_view(), name='booking-detail'),
    path("update/<int:booking_id>/",
         BookingUpdateView.as_view(), name='booking-update'),
    path("delete/<int:booking_id>/",
         BookingDeleteView.as_view(), name='booking-delete'),
    path("signup/", UserCreateView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token-referesh'),
]
