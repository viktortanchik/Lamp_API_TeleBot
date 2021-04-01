from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer


##################################################### Скрипт 1 #####################################################
class Script_1_listserializer(serializers.ModelSerializer):
    #Scripts = ProgramLamps1listSerializer(read_only=True, many=True)
    class Meta:
        model = Script_1
        fields = '__all__'

class Script_1_DetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Script_1
        fields = '__all__'
##################################################### Скрипт 2 #####################################################
class Script_2_listserializer(serializers.ModelSerializer):
    #Scripts = ProgramLamps1listSerializer(read_only=True, many=True)
    class Meta:
        model = Script_2
        fields = '__all__'

class Script_2_DetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Script_2
        fields = '__all__'
##################################################### Скрипт 3 #####################################################
class Script_3_listserializer(serializers.ModelSerializer):
    #Scripts = ProgramLamps1listSerializer(read_only=True, many=True)
    class Meta:
        model = Script_3
        fields = '__all__'

class Script_3_DetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Script_3
        fields = '__all__'
#############################################  Родитель Скриптов  ##########################
class Scriptslistserializer(serializers.ModelSerializer):
    Script_1 = Script_1_listserializer(read_only=True, many=True)
    Script_2 = Script_2_listserializer(read_only=True, many=True)
    Script_3 = Script_3_listserializer(read_only=True, many=True)

    class Meta:
        model = Scripts
        fields = '__all__'#('Script_1','Script_2','Script_3',)

class ScriptsDetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Scripts
        fields = '__all__'
################################################################################

######################################################################
class LampslistSerializer(ModelSerializer):
    Scripts = Scriptslistserializer(read_only=True, many=True)

    class Meta:
        model = Lamps
        fields = '__all__'#('id', 'status', 'mode', 'Scripts') #album_musician

class LampsDetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Lamps
        fields = '__all__'
##############################################################################
class ProgramLamps1DetailSerializer(serializers.ModelSerializer):
    #pixel_1_red = LampsDetailSerializer(many=True, read_only=True)
    class Meta:
        model = ProgramLamps1
        fields = '__all__'

class ProgramLamps1listSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramLamps1
        fields = ('pixel_1_red', 'pixel_1_green', 'pixel_1_blue')







