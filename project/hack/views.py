from django.shortcuts import render
from .models import *
from .serialisers import *
from rest_framework import generics

class dataListCreateView(generics.ListCreateAPIView):
    queryset = data.objects.all()
    serializer_class = dataSerialiser

        
class dataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =data.objects.all()
    serializer_class = dataSerialiser   
