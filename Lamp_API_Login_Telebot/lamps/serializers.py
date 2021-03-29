from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer


"""
class ProgramLamps1DetailSerializer(serializers.ModelSerializer):
    #pixel_1_red = LampsDetailSerializer(many=True, read_only=True)
    class Meta:
        model = ProgramLamps1
        fields = '__all__'
        """

class ProgramLamps1listSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramLamps1
        fields = ('pixel_1_red', 'pixel_1_green', 'pixel_1_blue')

class LampslistSerializer(ModelSerializer):
    album_musician = ProgramLamps1listSerializer(read_only=True, many=True)

    class Meta:
        model = Lamps
        fields = ('id', 'status', 'mode', 'red', 'green', 'blue','album_musician')

"""
class LampsDetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Lamps
        fields = '__all__'
"""







