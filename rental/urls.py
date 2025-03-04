from django.urls import path
from .views import BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('booking/', BookingListCreateAPIView.as_view(), name='list-create-booking'),
    path('booking/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-booking'),
    
]