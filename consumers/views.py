from django.shortcuts import render, reverse
from .models import Profile
from .serializers import ConsumerSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from Agency.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

@api_view(['POST'])
def consumer_view(request):
    # consumer_serializer = ConsumerSerializer(data=request.data)

    # print(request.data)
    if request.method == 'POST':
        consumer_data = JSONParser().parse(request)

        if consumer_data["type"] == 'login':
            user = authenticate(request, username=consumer_data["consumer_name"],
                                password=consumer_data["password"])
            if user is not None:
                return  JsonResponse({'Authentication': 'success', 'consumer_no': user.profile.consumer_no, 'email': user.profile.email, 'phone': user.profile.phone_no})
            else:
                return JsonResponse({'Authentication': 'fail'}, status=status.HTTP_400_BAD_REQUEST)


        if consumer_data["type"] == 'register':
            user = User.objects.create_user(username=consumer_data["consumer_name"],
                                            password=consumer_data["password"])
            user.profile.email=consumer_data["email"]
            user.profile.phone_no=consumer_data["phone_no"]
            user.profile.consumer_no=consumer_data["consumer_no"]
            user.save()
            subject = "Welcome to Gas Booking"
            message = consumer_data["consumer_name"] + " Your Account has been Created.Thanks for Using our product"
            recipent = consumer_data["email"]
            send_mail(subject, message, EMAIL_HOST_USER, [recipent], fail_silently=False)
            return JsonResponse({'Registration': 'success'})
