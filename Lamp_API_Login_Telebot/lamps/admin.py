from django.contrib import admin
from .models import *


#admin.site.register(ProgramLamps1)
admin.site.register(Lamps)
admin.site.register(Humidity_Temperature)
admin.site.register(Scripts)
admin.site.register(Script_1)
admin.site.register(Script_2)
admin.site.register(Script_3)


#admin.site.register(ProgramLamps1)

'''
class Subscriberadmin (admin.ModelAdmin):
    class Meta:
        model = ProgramLamps1
'''

