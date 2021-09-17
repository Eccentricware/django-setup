#from django.shortcuts import render
from readings.models import Reading
from readings.serializers import ReadingSerializer
from rest_framework import generics

class ReadingList(generics.ListCreateAPIView):
  queryset = Reading.objects.all()
  serializer_class = ReadingSerializer

class ReadingDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Reading.objects.all()
  serializer_class = ReadingSerializer
