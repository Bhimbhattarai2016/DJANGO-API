
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render


from django.http import HttpResponse
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth import authenticate

from .serializers import UserRegistrationSerializer,UserLoginSerializer


# Create your views here.

def bhim(request):
    return HttpResponse("DJANGO is working properly and this is <h1>HomePage</h1>")


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Successful.'}, status=status.HTTP_201_CREATED)
             
             
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({'msg': 'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'none_field_errors':['गलत छ मुजि, फेरी हेर ']}}, status=status.HTTP_404_NOT_FOUND)
