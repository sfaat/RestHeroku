from django.shortcuts import render
from .serializers import *
from rest_framework import serializers
from rest_framework import mixins,generics
# Create your views here.
from .models import * 


class StudentCreateAPIView(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSrializers

class StudentAPIView(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSrializers    
