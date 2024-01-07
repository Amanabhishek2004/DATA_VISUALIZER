from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class DataUpdaeDelete(generics.RetrieveUpdateDestroyAPIView):
       
       queryset = CompanyData.objects.all()
       serializer_class = data_serializer



class Dataviewcreate_api(generics.ListCreateAPIView):
       
       queryset = CompanyData.objects.all()
       serializer_class = data_serializer


              

