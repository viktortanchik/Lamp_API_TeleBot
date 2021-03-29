from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import*
# Create your views here.

class LampsCreateView(generics.CreateAPIView):
    #serializer_class = LampsDetailSerializer
    serializer_class = LampslistSerializer

class LampsListView(generics.ListAPIView):
    serializer_class = LampslistSerializer
    queryset = Lamps.objects.all()

class LampsDtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LampslistSerializer
    queryset = Lamps.objects.all()
############################
class pixCreateView(generics.CreateAPIView):
    #serializer_class = ProgramLamps1DetailSerializer
    serializer_class = ProgramLamps1listSerializer
class pixListView(generics.ListAPIView):
    serializer_class = ProgramLamps1listSerializer
    queryset = ProgramLamps1.objects.all()

class pixDtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProgramLamps1listSerializer
    queryset = ProgramLamps1.objects.all()

