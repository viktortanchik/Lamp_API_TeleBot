from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'lamps'
urlpatterns = [

    path('lamps/create/',LampsCreateView.as_view()),
    path('lamps/detail/<int:pk>/', LampsDtailView.as_view()),
    path('all', LampsListView.as_view()),
######################################################### DHT11 Humidity_Temperature ######################################################
    path('DHT11/create/', Humidity_TemperatureCreateView.as_view()),
    path('DHT11/detail/<int:pk>/', Humidity_TemperatureDtailView.as_view()),
    path('DHT11/all', Humidity_TemperatureListView.as_view()),

######################################################### Scripts ######################################################
    path('pix/Scripts/create/', ScriptsCreateView.as_view()),
    path('pix/Scripts/detail/<int:pk>/', ScriptsDtailView.as_view()),
    path('pix/Scripts/all', ScriptsListView.as_view()),
################################################################ Script 1  #############################################
    path('pix/Script_1/create/', Script_1CreateView.as_view()),
    path('pix/Script_1/detail/<int:pk>/', Script_1DtailView.as_view()),
    path('pix/Script_1/all', Script_1ListView.as_view()),
######################################################### Script 2  ########################
    path('pix/Script_2/create/', Script_2CreateView.as_view()),
    path('pix/Script_2/detail/<int:pk>/', Script_2DtailView.as_view()),
    path('pix/Script_2/all', Script_2ListView.as_view()),
######################################################### Script 3 ########################
    path('pix/Script_3/create/', Script_3CreateView.as_view()),
    path('pix/Script_3/detail/<int:pk>/', Script_3DtailView.as_view()),
    path('pix/Script_3/all', Script_3ListView.as_view()),

    #########################################################
    path('pix/create/', pixCreateView.as_view()),
    path('pix/detail/<int:pk>/', pixDtailView.as_view()),
    path('pix/all', pixListView.as_view()),
]