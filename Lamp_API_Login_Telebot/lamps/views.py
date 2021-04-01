from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import*
# Create your views here.
################################################################################################################
class LampsCreateView(generics.CreateAPIView):
    serializer_class = LampsDetailSerializer
    queryset = Lamps.objects.all()
    #serializer_class = LampslistSerializer

class LampsListView(generics.ListAPIView):
    serializer_class = LampslistSerializer
    queryset = Lamps.objects.all()

class LampsDtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LampslistSerializer
    queryset = Lamps.objects.all()
################################################################################################################
class pixCreateView(generics.CreateAPIView):
    serializer_class = ProgramLamps1DetailSerializer
    #serializer_class = ProgramLamps1listSerializer
class pixListView(generics.ListAPIView):
    serializer_class = ProgramLamps1listSerializer
    queryset = ProgramLamps1.objects.all()

class pixDtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProgramLamps1listSerializer
    queryset = ProgramLamps1.objects.all()

################################################################################################################

######################################################### Scripts View #######################################################
class ScriptsCreateView(generics.CreateAPIView):
    serializer_class = ScriptsDetailSerializer
    #serializer_class = ProgramLamps1listSerializer
class ScriptsListView(generics.ListAPIView):
    serializer_class = Scriptslistserializer
    queryset = Scripts.objects.all()

class ScriptsDtailView(generics.RetrieveUpdateDestroyAPIView):   #############
    serializer_class = Scriptslistserializer
    queryset = Scripts.objects.all()

#################################################################### Script 1 View ############################################
class Script_1CreateView(generics.CreateAPIView):
    serializer_class = Script_1_DetailSerializer
    #serializer_class = ProgramLamps1listSerializer
class Script_1ListView(generics.ListAPIView):
    serializer_class = Script_1_listserializer
    queryset = Script_1.objects.all()

class Script_1DtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Script_1_listserializer
    queryset = Script_1.objects.all()
#################################################################### Script 2 View ############################################
class Script_2CreateView(generics.CreateAPIView):
    serializer_class = Script_2_DetailSerializer
    #serializer_class = ProgramLamps1listSerializer
class Script_2ListView(generics.ListAPIView):
    serializer_class = Script_2_listserializer
    queryset = Script_2.objects.all()

class Script_2DtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Script_2_listserializer
    queryset = Script_2.objects.all()
###################################################################### Script 3 View ##########################################
class Script_3CreateView(generics.CreateAPIView):
    serializer_class = Script_3_DetailSerializer
    #serializer_class = ProgramLamps1listSerializer
class Script_3ListView(generics.ListAPIView):
    serializer_class = Script_3_listserializer
    queryset = Script_3.objects.all()

class Script_3DtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Script_1_listserializer
    queryset = Script_3.objects.all()
################################################################################################################


