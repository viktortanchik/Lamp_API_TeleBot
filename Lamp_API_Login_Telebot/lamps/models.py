from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Lamps(models.Model):
    vin = models.CharField(verbose_name='vin', db_index=True, unique=True, max_length=64)
    status = models.CharField(verbose_name='status', db_index=True, max_length=64)
    mode = models.CharField(verbose_name='mode', db_index=True,  max_length=64)
    red = models.CharField(verbose_name='red', db_index=True, max_length=64)
    green = models.CharField(verbose_name='green', db_index=True, max_length=64)
    blue = models.CharField(verbose_name='blue', db_index=True, max_length=64)

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
"""
    def __str__(self):
        return f'{[self.vin, self.status, self.mode, self.red,self.green, self.blue, self.user]!r}'
"""
class ProgramLamps1(models.Model):
    pixel_1_red = models.CharField(verbose_name='pixel_1_red',  max_length=64)
    pixel_1_green = models.CharField(verbose_name='pixel_1_green',  max_length=64)
    pixel_1_blue = models.CharField(verbose_name='pixel_1_blue',  max_length=64)
    artist = models.ForeignKey(Lamps, on_delete=models.CASCADE, related_name='album_musician', null=True, blank=True)

    #status = models.ForeignKey(Lamps,related_name='pix',on_delete=models.CASCADE)


""" def __str__(self):
     return f'{[self.pixel_1r, self.pixel_1_green, self.pixel_1_blue]!r}'"""


