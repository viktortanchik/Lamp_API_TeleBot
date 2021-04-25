from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Lamps(models.Model):
    vin = models.CharField(verbose_name='vin', db_index=True, unique=True, max_length=64)
    date = models.CharField(verbose_name='date', max_length=128, default='1')
    status = models.CharField(verbose_name='status', db_index=True, max_length=64,default='2')
    mode = models.CharField(verbose_name='mode', db_index=True, max_length=64,default='2')
    #H_T = models.CharField(verbose_name='H_T', max_length=128)

    red = models.CharField(verbose_name='red', db_index=True, default='100', max_length=64)
    green = models.CharField(verbose_name='green', db_index=True, default='100', max_length=64)
    blue = models.CharField(verbose_name='blue', db_index=True, default='100', max_length=64)

    #user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

###########################################################################

class Humidity_Temperature(models.Model):
    Humidity = models.CharField(verbose_name='Humidity', max_length=64, default='1')
    Temperature = models.CharField(verbose_name='Temperature', max_length=64, default='1')
    H_T = models.ForeignKey(Lamps, on_delete=models.CASCADE, related_name='H_T', null=True, blank=True)

class Scripts(models.Model):
    numbers = models.CharField(verbose_name='numbers', max_length=64)
    Scripts = models.ForeignKey(Lamps, on_delete=models.CASCADE, related_name='Scripts', null=True, blank=True)

    #Script_1 = models.CharField(verbose_name='Script_1', max_length=64)
    #Script_2 = models.CharField(verbose_name='Script_2', max_length=64)
    #Script_3 = models.CharField(verbose_name='Script_3', max_length=64)


    #Script_1 = models.ForeignKey(Script_1, on_delete=models.CASCADE, related_name='Script_1', null=True, blank=True)
    #Script_2 = models.ForeignKey(Script_2, on_delete=models.CASCADE, related_name='Script_2', null=True, blank=True)
    #Script_3 = models.ForeignKey(Script_3, on_delete=models.CASCADE, related_name='Script_3', null=True, blank=True)


class Script_1(models.Model):
    Script_1 = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='Script_1', null=True, blank=True)

    #########################
    pixel_1_red = models.CharField(verbose_name='pixel_1_red', max_length=64,default='100')
    pixel_1_green = models.CharField(verbose_name='pixel_1_green', max_length=64,default='100')
    pixel_1_blue = models.CharField(verbose_name='pixel_1_blue', max_length=64,default='100')
    #########################
    pixel_2_red = models.CharField(verbose_name='pixel_2_red', max_length=64,default='100')
    pixel_2_green = models.CharField(verbose_name='pixel_2_green', max_length=64,default='100')
    pixel_2_blue = models.CharField(verbose_name='pixel_2_blue', max_length=64,default='100')
    #########################
    pixel_3_red = models.CharField(verbose_name='pixel_3_red', max_length=64,default='100')
    pixel_3_green = models.CharField(verbose_name='pixel_3_green', max_length=64,default='100')
    pixel_3_blue = models.CharField(verbose_name='pixel_3_blue', max_length=64,default='100')
    #########################
    pixel_4_red = models.CharField(verbose_name='pixel_4_red', max_length=64 ,default='100')
    pixel_4_green = models.CharField(verbose_name='pixel_4_green', max_length=64 ,default='100')
    pixel_4_blue = models.CharField(verbose_name='pixel_4_blue', max_length=64 ,default='100')
    #########################
    pixel_5_red = models.CharField(verbose_name='pixel_5_red', max_length=64 ,default='100')
    pixel_5_green = models.CharField(verbose_name='pixel_5_green', max_length=64 ,default='100')
    pixel_5_blue = models.CharField(verbose_name='pixel_5_blue', max_length=64 ,default='100')
    #########################
    pixel_6_red = models.CharField(verbose_name='pixel_6_red', max_length=64 ,default='100')
    pixel_6_green = models.CharField(verbose_name='pixel_6_green', max_length=64 ,default='100')
    pixel_6_blue = models.CharField(verbose_name='pixel_6_blue', max_length=64 ,default='100')
    #########################
    pixel_7_red = models.CharField(verbose_name='pixel_7_red', max_length=64 ,default='100')
    pixel_7_green = models.CharField(verbose_name='pixel_7_green', max_length=64 ,default='100')
    pixel_7_blue = models.CharField(verbose_name='pixel_7_blue', max_length=64 ,default='100')
    #########################
    pixel_8_red = models.CharField(verbose_name='pixel_8_red', max_length=64 ,default='100')
    pixel_8_green = models.CharField(verbose_name='pixel_8_green', max_length=64 ,default='100')
    pixel_8_blue = models.CharField(verbose_name='pixel_8_blue', max_length=64 ,default='100')
    #########################
    pixel_9_red = models.CharField(verbose_name='pixel_9_red', max_length=64,default='100')
    pixel_9_green = models.CharField(verbose_name='pixel_9_green', max_length=64,default='100')
    pixel_9_blue = models.CharField(verbose_name='pixel_9_blue', max_length=64,default='100')
    #########################
    pixel_10_red = models.CharField(verbose_name='pixel_10_red', max_length=64,default='100')
    pixel_10_green = models.CharField(verbose_name='pixel_10_green', max_length=64,default='100')
    pixel_10_blue = models.CharField(verbose_name='pixel_10_blue', max_length=64,default='100')
    #########################
    pixel_11_red = models.CharField(verbose_name='pixel_11_red', max_length=64,default='100')
    pixel_11_green = models.CharField(verbose_name='pixel_11_green', max_length=64,default='100')
    pixel_11_blue = models.CharField(verbose_name='pixel_11_blue', max_length=64,default='100')
    #########################
    pixel_12_red = models.CharField(verbose_name='pixel_12_red', max_length=64,default='100')
    pixel_12_green = models.CharField(verbose_name='pixel_12_green', max_length=64,default='100')
    pixel_12_blue = models.CharField(verbose_name='pixel_12_blue', max_length=64,default='100')
    #########################
    pixel_13_red = models.CharField(verbose_name='pixel_13_red', max_length=64,default='100')
    pixel_13_green = models.CharField(verbose_name='pixel_13_green', max_length=64,default='100')
    pixel_13_blue = models.CharField(verbose_name='pixel_13_blue', max_length=64,default='100')
    #########################
    pixel_14_red = models.CharField(verbose_name='pixel_14_red', max_length=64,default='100')
    pixel_14_green = models.CharField(verbose_name='pixel_14_green', max_length=64,default='100')
    pixel_14_blue = models.CharField(verbose_name='pixel_14_blue', max_length=64,default='100')
    #########################
    pixel_15_red = models.CharField(verbose_name='pixel_15_red', max_length=64,default='100')
    pixel_15_green = models.CharField(verbose_name='pixel_15_green', max_length=64,default='100')
    pixel_15_blue = models.CharField(verbose_name='pixel_15_blue', max_length=64,default='100')
    #########################
    pixel_16_red = models.CharField(verbose_name='pixel_16_red', max_length=64,default='100')
    pixel_16_green = models.CharField(verbose_name='pixel_16_green', max_length=64,default='100')
    pixel_16_blue = models.CharField(verbose_name='pixel_16_blue', max_length=64,default='100')
    #########################
    pixel_17_red = models.CharField(verbose_name='pixel_17_red', max_length=64,default='100')
    pixel_17_green = models.CharField(verbose_name='pixel_17_green', max_length=64,default='100')
    pixel_17_blue = models.CharField(verbose_name='pixel_17_blue', max_length=64,default='100')
    #########################
    pixel_18_red = models.CharField(verbose_name='pixel_18_red', max_length=64,default='100')
    pixel_18_green = models.CharField(verbose_name='pixel_18_green', max_length=64,default='100')
    pixel_18_blue = models.CharField(verbose_name='pixel_18_blue', max_length=64,default='100')
    #########################
    pixel_19_red = models.CharField(verbose_name='pixel_19_red', max_length=64,default='100')
    pixel_19_green = models.CharField(verbose_name='pixel_19_green', max_length=64,default='100')
    pixel_19_blue = models.CharField(verbose_name='pixel_19_blue', max_length=64,default='100')
    #########################
    pixel_20_red = models.CharField(verbose_name='pixel_20_red', max_length=64,default='100')
    pixel_20_green = models.CharField(verbose_name='pixel_20_green', max_length=64,default='100')
    pixel_20_blue = models.CharField(verbose_name='pixel_20_blue', max_length=64,default='100')
 #########################
    pixel_21_red = models.CharField(verbose_name='pixel_21_red', max_length=64,default='100')
    pixel_21_green = models.CharField(verbose_name='pixel_21_green', max_length=64,default='100')
    pixel_21_blue = models.CharField(verbose_name='pixel_21_blue', max_length=64,default='100')
    #########################
    pixel_22_red = models.CharField(verbose_name='pixel_22_red', max_length=64,default='100')
    pixel_22_green = models.CharField(verbose_name='pixel_22_green', max_length=64,default='100')
    pixel_22_blue = models.CharField(verbose_name='pixel_22_blue', max_length=64,default='100')
    #########################
    pixel_23_red = models.CharField(verbose_name='pixel_23_red', max_length=64,default='100')
    pixel_23_green = models.CharField(verbose_name='pixel_23_green', max_length=64,default='100')
    pixel_23_blue = models.CharField(verbose_name='pixel_23_blue', max_length=64,default='100')
    #########################
    pixel_24_red = models.CharField(verbose_name='pixel_24_red', max_length=64,default='100')
    pixel_24_green = models.CharField(verbose_name='pixel_24_green', max_length=64,default='100')
    pixel_24_blue = models.CharField(verbose_name='pixel_24_blue', max_length=64,default='100')
    #########################
    pixel_25_red = models.CharField(verbose_name='pixel_25_red', max_length=64,default='100')
    pixel_25_green = models.CharField(verbose_name='pixel_25_green', max_length=64,default='100')
    pixel_25_blue = models.CharField(verbose_name='pixel_25_blue', max_length=64,default='100')
    #########################
    pixel_26_red = models.CharField(verbose_name='pixel_26_red', max_length=64,default='100')
    pixel_26_green = models.CharField(verbose_name='pixel_26_green', max_length=64,default='100')
    pixel_26_blue = models.CharField(verbose_name='pixel_26_blue', max_length=64,default='100')
    #########################
    pixel_27_red = models.CharField(verbose_name='pixel_27_red', max_length=64,default='100')
    pixel_27_green = models.CharField(verbose_name='pixel_27_green', max_length=64,default='100')
    pixel_27_blue = models.CharField(verbose_name='pixel_27_blue', max_length=64,default='100')
    #########################
    pixel_28_red = models.CharField(verbose_name='pixel_28_red', max_length=64,default='100')
    pixel_28_green = models.CharField(verbose_name='pixel_28_green', max_length=64,default='100')
    pixel_28_blue = models.CharField(verbose_name='pixel_28_blue', max_length=64,default='100')
    #########################
    pixel_29_red = models.CharField(verbose_name='pixel_29_red', max_length=64,default='100')
    pixel_29_green = models.CharField(verbose_name='pixel_29_green', max_length=64,default='100')
    pixel_29_blue = models.CharField(verbose_name='pixel_29_blue', max_length=64,default='100')
    #########################
    pixel_30_red = models.CharField(verbose_name='pixel_30_red', max_length=64,default='100')
    pixel_30_green = models.CharField(verbose_name='pixel_30_green', max_length=64,default='100')
    pixel_30_blue = models.CharField(verbose_name='pixel_30_blue', max_length=64,default='100')


class Script_2(models.Model):
    Script_2 = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='Script_2', null=True, blank=True)

    #########################
    pixel_1_red = models.CharField(verbose_name='pixel_1_red', max_length=64, default='100')
    pixel_1_green = models.CharField(verbose_name='pixel_1_green', max_length=64, default='100')
    pixel_1_blue = models.CharField(verbose_name='pixel_1_blue', max_length=64, default='100')
    #########################
    pixel_2_red = models.CharField(verbose_name='pixel_2_red', max_length=64, default='100')
    pixel_2_green = models.CharField(verbose_name='pixel_2_green', max_length=64, default='100')
    pixel_2_blue = models.CharField(verbose_name='pixel_2_blue', max_length=64, default='100')
    #########################
    pixel_3_red = models.CharField(verbose_name='pixel_3_red', max_length=64, default='100')
    pixel_3_green = models.CharField(verbose_name='pixel_3_green', max_length=64, default='100')
    pixel_3_blue = models.CharField(verbose_name='pixel_3_blue', max_length=64, default='100')
    #########################
    pixel_4_red = models.CharField(verbose_name='pixel_4_red', max_length=64, default='100')
    pixel_4_green = models.CharField(verbose_name='pixel_4_green', max_length=64, default='100')
    pixel_4_blue = models.CharField(verbose_name='pixel_4_blue', max_length=64, default='100')
    #########################
    pixel_5_red = models.CharField(verbose_name='pixel_5_red', max_length=64, default='100')
    pixel_5_green = models.CharField(verbose_name='pixel_5_green', max_length=64, default='100')
    pixel_5_blue = models.CharField(verbose_name='pixel_5_blue', max_length=64, default='100')
    #########################
    pixel_6_red = models.CharField(verbose_name='pixel_6_red', max_length=64, default='100')
    pixel_6_green = models.CharField(verbose_name='pixel_6_green', max_length=64, default='100')
    pixel_6_blue = models.CharField(verbose_name='pixel_6_blue', max_length=64, default='100')
    #########################
    pixel_7_red = models.CharField(verbose_name='pixel_7_red', max_length=64, default='100')
    pixel_7_green = models.CharField(verbose_name='pixel_7_green', max_length=64, default='100')
    pixel_7_blue = models.CharField(verbose_name='pixel_7_blue', max_length=64, default='100')
    #########################
    pixel_8_red = models.CharField(verbose_name='pixel_8_red', max_length=64, default='100')
    pixel_8_green = models.CharField(verbose_name='pixel_8_green', max_length=64, default='100')
    pixel_8_blue = models.CharField(verbose_name='pixel_8_blue', max_length=64, default='100')
    #########################
    pixel_9_red = models.CharField(verbose_name='pixel_9_red', max_length=64, default='100')
    pixel_9_green = models.CharField(verbose_name='pixel_9_green', max_length=64, default='100')
    pixel_9_blue = models.CharField(verbose_name='pixel_9_blue', max_length=64, default='100')
    #########################
    pixel_10_red = models.CharField(verbose_name='pixel_10_red', max_length=64, default='100')
    pixel_10_green = models.CharField(verbose_name='pixel_10_green', max_length=64, default='100')
    pixel_10_blue = models.CharField(verbose_name='pixel_10_blue', max_length=64, default='100')
    #########################
    pixel_11_red = models.CharField(verbose_name='pixel_11_red', max_length=64, default='100')
    pixel_11_green = models.CharField(verbose_name='pixel_11_green', max_length=64, default='100')
    pixel_11_blue = models.CharField(verbose_name='pixel_11_blue', max_length=64, default='100')
    #########################
    pixel_12_red = models.CharField(verbose_name='pixel_12_red', max_length=64, default='100')
    pixel_12_green = models.CharField(verbose_name='pixel_12_green', max_length=64, default='100')
    pixel_12_blue = models.CharField(verbose_name='pixel_12_blue', max_length=64, default='100')
    #########################
    pixel_13_red = models.CharField(verbose_name='pixel_13_red', max_length=64, default='100')
    pixel_13_green = models.CharField(verbose_name='pixel_13_green', max_length=64, default='100')
    pixel_13_blue = models.CharField(verbose_name='pixel_13_blue', max_length=64, default='100')
    #########################
    pixel_14_red = models.CharField(verbose_name='pixel_14_red', max_length=64, default='100')
    pixel_14_green = models.CharField(verbose_name='pixel_14_green', max_length=64, default='100')
    pixel_14_blue = models.CharField(verbose_name='pixel_14_blue', max_length=64, default='100')
    #########################
    pixel_15_red = models.CharField(verbose_name='pixel_15_red', max_length=64, default='100')
    pixel_15_green = models.CharField(verbose_name='pixel_15_green', max_length=64, default='100')
    pixel_15_blue = models.CharField(verbose_name='pixel_15_blue', max_length=64, default='100')
    #########################
    pixel_16_red = models.CharField(verbose_name='pixel_16_red', max_length=64, default='100')
    pixel_16_green = models.CharField(verbose_name='pixel_16_green', max_length=64, default='100')
    pixel_16_blue = models.CharField(verbose_name='pixel_16_blue', max_length=64, default='100')
    #########################
    pixel_17_red = models.CharField(verbose_name='pixel_17_red', max_length=64, default='100')
    pixel_17_green = models.CharField(verbose_name='pixel_17_green', max_length=64, default='100')
    pixel_17_blue = models.CharField(verbose_name='pixel_17_blue', max_length=64, default='100')
    #########################
    pixel_18_red = models.CharField(verbose_name='pixel_18_red', max_length=64, default='100')
    pixel_18_green = models.CharField(verbose_name='pixel_18_green', max_length=64, default='100')
    pixel_18_blue = models.CharField(verbose_name='pixel_18_blue', max_length=64, default='100')
    #########################
    pixel_19_red = models.CharField(verbose_name='pixel_19_red', max_length=64, default='100')
    pixel_19_green = models.CharField(verbose_name='pixel_19_green', max_length=64, default='100')
    pixel_19_blue = models.CharField(verbose_name='pixel_19_blue', max_length=64, default='100')
    #########################
    pixel_20_red = models.CharField(verbose_name='pixel_20_red', max_length=64, default='100')
    pixel_20_green = models.CharField(verbose_name='pixel_20_green', max_length=64, default='100')
    pixel_20_blue = models.CharField(verbose_name='pixel_20_blue', max_length=64, default='100')
    #########################
    pixel_21_red = models.CharField(verbose_name='pixel_21_red', max_length=64, default='100')
    pixel_21_green = models.CharField(verbose_name='pixel_21_green', max_length=64, default='100')
    pixel_21_blue = models.CharField(verbose_name='pixel_21_blue', max_length=64, default='100')
    #########################
    pixel_22_red = models.CharField(verbose_name='pixel_22_red', max_length=64, default='100')
    pixel_22_green = models.CharField(verbose_name='pixel_22_green', max_length=64, default='100')
    pixel_22_blue = models.CharField(verbose_name='pixel_22_blue', max_length=64, default='100')
    #########################
    pixel_23_red = models.CharField(verbose_name='pixel_23_red', max_length=64, default='100')
    pixel_23_green = models.CharField(verbose_name='pixel_23_green', max_length=64, default='100')
    pixel_23_blue = models.CharField(verbose_name='pixel_23_blue', max_length=64, default='100')
    #########################
    pixel_24_red = models.CharField(verbose_name='pixel_24_red', max_length=64, default='100')
    pixel_24_green = models.CharField(verbose_name='pixel_24_green', max_length=64, default='100')
    pixel_24_blue = models.CharField(verbose_name='pixel_24_blue', max_length=64, default='100')
    #########################
    pixel_25_red = models.CharField(verbose_name='pixel_25_red', max_length=64, default='100')
    pixel_25_green = models.CharField(verbose_name='pixel_25_green', max_length=64, default='100')
    pixel_25_blue = models.CharField(verbose_name='pixel_25_blue', max_length=64, default='100')
    #########################
    pixel_26_red = models.CharField(verbose_name='pixel_26_red', max_length=64, default='100')
    pixel_26_green = models.CharField(verbose_name='pixel_26_green', max_length=64, default='100')
    pixel_26_blue = models.CharField(verbose_name='pixel_26_blue', max_length=64, default='100')
    #########################
    pixel_27_red = models.CharField(verbose_name='pixel_27_red', max_length=64, default='100')
    pixel_27_green = models.CharField(verbose_name='pixel_27_green', max_length=64, default='100')
    pixel_27_blue = models.CharField(verbose_name='pixel_27_blue', max_length=64, default='100')
    #########################
    pixel_28_red = models.CharField(verbose_name='pixel_28_red', max_length=64, default='100')
    pixel_28_green = models.CharField(verbose_name='pixel_28_green', max_length=64, default='100')
    pixel_28_blue = models.CharField(verbose_name='pixel_28_blue', max_length=64, default='100')
    #########################
    pixel_29_red = models.CharField(verbose_name='pixel_29_red', max_length=64, default='100')
    pixel_29_green = models.CharField(verbose_name='pixel_29_green', max_length=64, default='100')
    pixel_29_blue = models.CharField(verbose_name='pixel_29_blue', max_length=64, default='100')
    #########################
    pixel_30_red = models.CharField(verbose_name='pixel_30_red', max_length=64, default='100')
    pixel_30_green = models.CharField(verbose_name='pixel_30_green', max_length=64, default='100')
    pixel_30_blue = models.CharField(verbose_name='pixel_30_blue', max_length=64, default='100')


class Script_3(models.Model):
    Script_3 = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='Script_3', null=True, blank=True)

    #########################
    pixel_1_red = models.CharField(verbose_name='pixel_1_red', max_length=64, default='100')
    pixel_1_green = models.CharField(verbose_name='pixel_1_green', max_length=64, default='100')
    pixel_1_blue = models.CharField(verbose_name='pixel_1_blue', max_length=64, default='100')
    #########################
    pixel_2_red = models.CharField(verbose_name='pixel_2_red', max_length=64, default='100')
    pixel_2_green = models.CharField(verbose_name='pixel_2_green', max_length=64, default='100')
    pixel_2_blue = models.CharField(verbose_name='pixel_2_blue', max_length=64, default='100')
    #########################
    pixel_3_red = models.CharField(verbose_name='pixel_3_red', max_length=64, default='100')
    pixel_3_green = models.CharField(verbose_name='pixel_3_green', max_length=64, default='100')
    pixel_3_blue = models.CharField(verbose_name='pixel_3_blue', max_length=64, default='100')
    #########################
    pixel_4_red = models.CharField(verbose_name='pixel_4_red', max_length=64, default='100')
    pixel_4_green = models.CharField(verbose_name='pixel_4_green', max_length=64, default='100')
    pixel_4_blue = models.CharField(verbose_name='pixel_4_blue', max_length=64, default='100')
    #########################
    pixel_5_red = models.CharField(verbose_name='pixel_5_red', max_length=64, default='100')
    pixel_5_green = models.CharField(verbose_name='pixel_5_green', max_length=64, default='100')
    pixel_5_blue = models.CharField(verbose_name='pixel_5_blue', max_length=64, default='100')
    #########################
    pixel_6_red = models.CharField(verbose_name='pixel_6_red', max_length=64, default='100')
    pixel_6_green = models.CharField(verbose_name='pixel_6_green', max_length=64, default='100')
    pixel_6_blue = models.CharField(verbose_name='pixel_6_blue', max_length=64, default='100')
    #########################
    pixel_7_red = models.CharField(verbose_name='pixel_7_red', max_length=64, default='100')
    pixel_7_green = models.CharField(verbose_name='pixel_7_green', max_length=64, default='100')
    pixel_7_blue = models.CharField(verbose_name='pixel_7_blue', max_length=64, default='100')
    #########################
    pixel_8_red = models.CharField(verbose_name='pixel_8_red', max_length=64, default='100')
    pixel_8_green = models.CharField(verbose_name='pixel_8_green', max_length=64, default='100')
    pixel_8_blue = models.CharField(verbose_name='pixel_8_blue', max_length=64, default='100')
    #########################
    pixel_9_red = models.CharField(verbose_name='pixel_9_red', max_length=64, default='100')
    pixel_9_green = models.CharField(verbose_name='pixel_9_green', max_length=64, default='100')
    pixel_9_blue = models.CharField(verbose_name='pixel_9_blue', max_length=64, default='100')
    #########################
    pixel_10_red = models.CharField(verbose_name='pixel_10_red', max_length=64, default='100')
    pixel_10_green = models.CharField(verbose_name='pixel_10_green', max_length=64, default='100')
    pixel_10_blue = models.CharField(verbose_name='pixel_10_blue', max_length=64, default='100')
    #########################
    pixel_11_red = models.CharField(verbose_name='pixel_11_red', max_length=64, default='100')
    pixel_11_green = models.CharField(verbose_name='pixel_11_green', max_length=64, default='100')
    pixel_11_blue = models.CharField(verbose_name='pixel_11_blue', max_length=64, default='100')
    #########################
    pixel_12_red = models.CharField(verbose_name='pixel_12_red', max_length=64, default='100')
    pixel_12_green = models.CharField(verbose_name='pixel_12_green', max_length=64, default='100')
    pixel_12_blue = models.CharField(verbose_name='pixel_12_blue', max_length=64, default='100')
    #########################
    pixel_13_red = models.CharField(verbose_name='pixel_13_red', max_length=64, default='100')
    pixel_13_green = models.CharField(verbose_name='pixel_13_green', max_length=64, default='100')
    pixel_13_blue = models.CharField(verbose_name='pixel_13_blue', max_length=64, default='100')
    #########################
    pixel_14_red = models.CharField(verbose_name='pixel_14_red', max_length=64, default='100')
    pixel_14_green = models.CharField(verbose_name='pixel_14_green', max_length=64, default='100')
    pixel_14_blue = models.CharField(verbose_name='pixel_14_blue', max_length=64, default='100')
    #########################
    pixel_15_red = models.CharField(verbose_name='pixel_15_red', max_length=64, default='100')
    pixel_15_green = models.CharField(verbose_name='pixel_15_green', max_length=64, default='100')
    pixel_15_blue = models.CharField(verbose_name='pixel_15_blue', max_length=64, default='100')
    #########################
    pixel_16_red = models.CharField(verbose_name='pixel_16_red', max_length=64, default='100')
    pixel_16_green = models.CharField(verbose_name='pixel_16_green', max_length=64, default='100')
    pixel_16_blue = models.CharField(verbose_name='pixel_16_blue', max_length=64, default='100')
    #########################
    pixel_17_red = models.CharField(verbose_name='pixel_17_red', max_length=64, default='100')
    pixel_17_green = models.CharField(verbose_name='pixel_17_green', max_length=64, default='100')
    pixel_17_blue = models.CharField(verbose_name='pixel_17_blue', max_length=64, default='100')
    #########################
    pixel_18_red = models.CharField(verbose_name='pixel_18_red', max_length=64, default='100')
    pixel_18_green = models.CharField(verbose_name='pixel_18_green', max_length=64, default='100')
    pixel_18_blue = models.CharField(verbose_name='pixel_18_blue', max_length=64, default='100')
    #########################
    pixel_19_red = models.CharField(verbose_name='pixel_19_red', max_length=64, default='100')
    pixel_19_green = models.CharField(verbose_name='pixel_19_green', max_length=64, default='100')
    pixel_19_blue = models.CharField(verbose_name='pixel_19_blue', max_length=64, default='100')
    #########################
    pixel_20_red = models.CharField(verbose_name='pixel_20_red', max_length=64, default='100')
    pixel_20_green = models.CharField(verbose_name='pixel_20_green', max_length=64, default='100')
    pixel_20_blue = models.CharField(verbose_name='pixel_20_blue', max_length=64, default='100')
    #########################
    pixel_21_red = models.CharField(verbose_name='pixel_21_red', max_length=64, default='100')
    pixel_21_green = models.CharField(verbose_name='pixel_21_green', max_length=64, default='100')
    pixel_21_blue = models.CharField(verbose_name='pixel_21_blue', max_length=64, default='100')
    #########################
    pixel_22_red = models.CharField(verbose_name='pixel_22_red', max_length=64, default='100')
    pixel_22_green = models.CharField(verbose_name='pixel_22_green', max_length=64, default='100')
    pixel_22_blue = models.CharField(verbose_name='pixel_22_blue', max_length=64, default='100')
    #########################
    pixel_23_red = models.CharField(verbose_name='pixel_23_red', max_length=64, default='100')
    pixel_23_green = models.CharField(verbose_name='pixel_23_green', max_length=64, default='100')
    pixel_23_blue = models.CharField(verbose_name='pixel_23_blue', max_length=64, default='100')
    #########################
    pixel_24_red = models.CharField(verbose_name='pixel_24_red', max_length=64, default='100')
    pixel_24_green = models.CharField(verbose_name='pixel_24_green', max_length=64, default='100')
    pixel_24_blue = models.CharField(verbose_name='pixel_24_blue', max_length=64, default='100')
    #########################
    pixel_25_red = models.CharField(verbose_name='pixel_25_red', max_length=64, default='100')
    pixel_25_green = models.CharField(verbose_name='pixel_25_green', max_length=64, default='100')
    pixel_25_blue = models.CharField(verbose_name='pixel_25_blue', max_length=64, default='100')
    #########################
    pixel_26_red = models.CharField(verbose_name='pixel_26_red', max_length=64, default='100')
    pixel_26_green = models.CharField(verbose_name='pixel_26_green', max_length=64, default='100')
    pixel_26_blue = models.CharField(verbose_name='pixel_26_blue', max_length=64, default='100')
    #########################
    pixel_27_red = models.CharField(verbose_name='pixel_27_red', max_length=64, default='100')
    pixel_27_green = models.CharField(verbose_name='pixel_27_green', max_length=64, default='100')
    pixel_27_blue = models.CharField(verbose_name='pixel_27_blue', max_length=64, default='100')
    #########################
    pixel_28_red = models.CharField(verbose_name='pixel_28_red', max_length=64, default='100')
    pixel_28_green = models.CharField(verbose_name='pixel_28_green', max_length=64, default='100')
    pixel_28_blue = models.CharField(verbose_name='pixel_28_blue', max_length=64, default='100')
    #########################
    pixel_29_red = models.CharField(verbose_name='pixel_29_red', max_length=64, default='100')
    pixel_29_green = models.CharField(verbose_name='pixel_29_green', max_length=64, default='100')
    pixel_29_blue = models.CharField(verbose_name='pixel_29_blue', max_length=64, default='100')
    #########################
    pixel_30_red = models.CharField(verbose_name='pixel_30_red', max_length=64, default='100')
    pixel_30_green = models.CharField(verbose_name='pixel_30_green', max_length=64, default='100')
    pixel_30_blue = models.CharField(verbose_name='pixel_30_blue', max_length=64, default='100')


class ProgramLamps1(models.Model):
    #Script_4 = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='Script_4', null=True, blank=True)

    pixel_1_red = models.CharField(verbose_name='pixel_1_red',  max_length=64)
    pixel_1_green = models.CharField(verbose_name='pixel_1_green',  max_length=64)
    pixel_1_blue = models.CharField(verbose_name='pixel_1_blue',  max_length=64)
    #Lamps = models.ForeignKey(Lamps, on_delete=models.CASCADE, related_name='Program', null=True, blank=True)

    #status = models.ForeignKey(Lamps,related_name='pix',on_delete=models.CASCADE)

###########################################################################
