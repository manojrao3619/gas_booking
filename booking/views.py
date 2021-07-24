from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.core import serializers
 
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.decorators import api_view
import datetime

@api_view(['POST'])
def booking(request):
	if request.method == 'POST':
		booking_serializer = BookingSerializer(data=request.data)
		if booking_serializer.is_valid():
			booking = Booking.objects.create(consumer_name = booking_serializer.data['consumer_name'], 
 											 consumer_no   = booking_serializer.data['consumer_no'],
 											 phone_no      = booking_serializer.data['phone_no'],
 											 date   = datetime.datetime.now().strftime("%Y-%m-%d"),
 											 time   = datetime.datetime.now().strftime("%H:%M:%S"),
 											 status = "Booked"
				    )
			booking.save()
			return JsonResponse({'consumer_no' : booking.consumer_no, 'status': booking.status}, status=status.HTTP_201_CREATED) 
		return JsonResponse(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cancelBooking(request):
	if request.method == 'POST':
		booking_data = JSONParser().parse(request)
		try:
			booking = Booking.objects.get(consumer_no = booking_data['consumer_no'])
			if booking.status == 'Cancelled':
				return JsonResponse({'error': 'Booking already cancelled'}, status = status.HTTP_400_BAD_REQUEST)
			booking.status = 'Cancelled'
			booking.save()
			return JsonResponse({'Status': booking.status}, status = status.HTTP_201_CREATED)
		except:
			return JsonResponse({'Error': 'User not found'}, status = status.HTTP_400_BAD_REQUEST)
		
@api_view(['GET'])
def bookingHistory(request):
	if request.method == 'GET':
		consumer = request.GET.get("consumer")
		try:
			bookings = Booking.objects.filter(consumer_no = consumer)
			history =  serializers.serialize('json', bookings, fields=('model', 'pk'))
			return HttpResponse(history, content_type="text/json-comment-filtered")
		except:
			return JsonResponse({'Error': 'User not found'}, status = status.HTTP_400_BAD_REQUEST)
						
