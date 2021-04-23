# Generated by Django 3.1.7 on 2021-04-20 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lamps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='vin')),
                ('date', models.CharField(default='1', max_length=128, verbose_name='date')),
                ('status', models.CharField(db_index=True, default='2', max_length=64, verbose_name='status')),
                ('mode', models.CharField(db_index=True, default='2', max_length=64, verbose_name='mode')),
                ('red', models.CharField(db_index=True, default='100', max_length=64, verbose_name='red')),
                ('green', models.CharField(db_index=True, default='100', max_length=64, verbose_name='green')),
                ('blue', models.CharField(db_index=True, default='100', max_length=64, verbose_name='blue')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramLamps1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pixel_1_red', models.CharField(max_length=64, verbose_name='pixel_1_red')),
                ('pixel_1_green', models.CharField(max_length=64, verbose_name='pixel_1_green')),
                ('pixel_1_blue', models.CharField(max_length=64, verbose_name='pixel_1_blue')),
            ],
        ),
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=64, verbose_name='numbers')),
                ('Scripts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Scripts', to='lamps.lamps')),
            ],
        ),
        migrations.CreateModel(
            name='Script_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pixel_1_red', models.CharField(default='100', max_length=64, verbose_name='pixel_1_red')),
                ('pixel_1_green', models.CharField(default='100', max_length=64, verbose_name='pixel_1_green')),
                ('pixel_1_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_1_blue')),
                ('pixel_2_red', models.CharField(default='100', max_length=64, verbose_name='pixel_2_red')),
                ('pixel_2_green', models.CharField(default='100', max_length=64, verbose_name='pixel_2_green')),
                ('pixel_2_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_2_blue')),
                ('pixel_3_red', models.CharField(default='100', max_length=64, verbose_name='pixel_3_red')),
                ('pixel_3_green', models.CharField(default='100', max_length=64, verbose_name='pixel_3_green')),
                ('pixel_3_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_3_blue')),
                ('pixel_4_red', models.CharField(default='100', max_length=64, verbose_name='pixel_4_red')),
                ('pixel_4_green', models.CharField(default='100', max_length=64, verbose_name='pixel_4_green')),
                ('pixel_4_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_4_blue')),
                ('pixel_5_red', models.CharField(default='100', max_length=64, verbose_name='pixel_5_red')),
                ('pixel_5_green', models.CharField(default='100', max_length=64, verbose_name='pixel_5_green')),
                ('pixel_5_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_5_blue')),
                ('pixel_6_red', models.CharField(default='100', max_length=64, verbose_name='pixel_6_red')),
                ('pixel_6_green', models.CharField(default='100', max_length=64, verbose_name='pixel_6_green')),
                ('pixel_6_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_6_blue')),
                ('pixel_7_red', models.CharField(default='100', max_length=64, verbose_name='pixel_7_red')),
                ('pixel_7_green', models.CharField(default='100', max_length=64, verbose_name='pixel_7_green')),
                ('pixel_7_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_7_blue')),
                ('pixel_8_red', models.CharField(default='100', max_length=64, verbose_name='pixel_8_red')),
                ('pixel_8_green', models.CharField(default='100', max_length=64, verbose_name='pixel_8_green')),
                ('pixel_8_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_8_blue')),
                ('pixel_9_red', models.CharField(default='100', max_length=64, verbose_name='pixel_9_red')),
                ('pixel_9_green', models.CharField(default='100', max_length=64, verbose_name='pixel_9_green')),
                ('pixel_9_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_9_blue')),
                ('pixel_10_red', models.CharField(default='100', max_length=64, verbose_name='pixel_10_red')),
                ('pixel_10_green', models.CharField(default='100', max_length=64, verbose_name='pixel_10_green')),
                ('pixel_10_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_10_blue')),
                ('pixel_11_red', models.CharField(default='100', max_length=64, verbose_name='pixel_11_red')),
                ('pixel_11_green', models.CharField(default='100', max_length=64, verbose_name='pixel_11_green')),
                ('pixel_11_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_11_blue')),
                ('pixel_12_red', models.CharField(default='100', max_length=64, verbose_name='pixel_12_red')),
                ('pixel_12_green', models.CharField(default='100', max_length=64, verbose_name='pixel_12_green')),
                ('pixel_12_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_12_blue')),
                ('pixel_13_red', models.CharField(default='100', max_length=64, verbose_name='pixel_13_red')),
                ('pixel_13_green', models.CharField(default='100', max_length=64, verbose_name='pixel_13_green')),
                ('pixel_13_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_13_blue')),
                ('pixel_14_red', models.CharField(default='100', max_length=64, verbose_name='pixel_14_red')),
                ('pixel_14_green', models.CharField(default='100', max_length=64, verbose_name='pixel_14_green')),
                ('pixel_14_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_14_blue')),
                ('pixel_15_red', models.CharField(default='100', max_length=64, verbose_name='pixel_15_red')),
                ('pixel_15_green', models.CharField(default='100', max_length=64, verbose_name='pixel_15_green')),
                ('pixel_15_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_15_blue')),
                ('pixel_16_red', models.CharField(default='100', max_length=64, verbose_name='pixel_16_red')),
                ('pixel_16_green', models.CharField(default='100', max_length=64, verbose_name='pixel_16_green')),
                ('pixel_16_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_16_blue')),
                ('pixel_17_red', models.CharField(default='100', max_length=64, verbose_name='pixel_17_red')),
                ('pixel_17_green', models.CharField(default='100', max_length=64, verbose_name='pixel_17_green')),
                ('pixel_17_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_17_blue')),
                ('pixel_18_red', models.CharField(default='100', max_length=64, verbose_name='pixel_18_red')),
                ('pixel_18_green', models.CharField(default='100', max_length=64, verbose_name='pixel_18_green')),
                ('pixel_18_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_18_blue')),
                ('pixel_19_red', models.CharField(default='100', max_length=64, verbose_name='pixel_19_red')),
                ('pixel_19_green', models.CharField(default='100', max_length=64, verbose_name='pixel_19_green')),
                ('pixel_19_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_19_blue')),
                ('pixel_20_red', models.CharField(default='100', max_length=64, verbose_name='pixel_20_red')),
                ('pixel_20_green', models.CharField(default='100', max_length=64, verbose_name='pixel_20_green')),
                ('pixel_20_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_20_blue')),
                ('pixel_21_red', models.CharField(default='100', max_length=64, verbose_name='pixel_21_red')),
                ('pixel_21_green', models.CharField(default='100', max_length=64, verbose_name='pixel_21_green')),
                ('pixel_21_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_21_blue')),
                ('pixel_22_red', models.CharField(default='100', max_length=64, verbose_name='pixel_22_red')),
                ('pixel_22_green', models.CharField(default='100', max_length=64, verbose_name='pixel_22_green')),
                ('pixel_22_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_22_blue')),
                ('pixel_23_red', models.CharField(default='100', max_length=64, verbose_name='pixel_23_red')),
                ('pixel_23_green', models.CharField(default='100', max_length=64, verbose_name='pixel_23_green')),
                ('pixel_23_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_23_blue')),
                ('pixel_24_red', models.CharField(default='100', max_length=64, verbose_name='pixel_24_red')),
                ('pixel_24_green', models.CharField(default='100', max_length=64, verbose_name='pixel_24_green')),
                ('pixel_24_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_24_blue')),
                ('pixel_25_red', models.CharField(default='100', max_length=64, verbose_name='pixel_25_red')),
                ('pixel_25_green', models.CharField(default='100', max_length=64, verbose_name='pixel_25_green')),
                ('pixel_25_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_25_blue')),
                ('pixel_26_red', models.CharField(default='100', max_length=64, verbose_name='pixel_26_red')),
                ('pixel_26_green', models.CharField(default='100', max_length=64, verbose_name='pixel_26_green')),
                ('pixel_26_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_26_blue')),
                ('pixel_27_red', models.CharField(default='100', max_length=64, verbose_name='pixel_27_red')),
                ('pixel_27_green', models.CharField(default='100', max_length=64, verbose_name='pixel_27_green')),
                ('pixel_27_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_27_blue')),
                ('pixel_28_red', models.CharField(default='100', max_length=64, verbose_name='pixel_28_red')),
                ('pixel_28_green', models.CharField(default='100', max_length=64, verbose_name='pixel_28_green')),
                ('pixel_28_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_28_blue')),
                ('pixel_29_red', models.CharField(default='100', max_length=64, verbose_name='pixel_29_red')),
                ('pixel_29_green', models.CharField(default='100', max_length=64, verbose_name='pixel_29_green')),
                ('pixel_29_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_29_blue')),
                ('pixel_30_red', models.CharField(default='100', max_length=64, verbose_name='pixel_30_red')),
                ('pixel_30_green', models.CharField(default='100', max_length=64, verbose_name='pixel_30_green')),
                ('pixel_30_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_30_blue')),
                ('Script_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Script_3', to='lamps.scripts')),
            ],
        ),
        migrations.CreateModel(
            name='Script_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pixel_1_red', models.CharField(default='100', max_length=64, verbose_name='pixel_1_red')),
                ('pixel_1_green', models.CharField(default='100', max_length=64, verbose_name='pixel_1_green')),
                ('pixel_1_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_1_blue')),
                ('pixel_2_red', models.CharField(default='100', max_length=64, verbose_name='pixel_2_red')),
                ('pixel_2_green', models.CharField(default='100', max_length=64, verbose_name='pixel_2_green')),
                ('pixel_2_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_2_blue')),
                ('pixel_3_red', models.CharField(default='100', max_length=64, verbose_name='pixel_3_red')),
                ('pixel_3_green', models.CharField(default='100', max_length=64, verbose_name='pixel_3_green')),
                ('pixel_3_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_3_blue')),
                ('pixel_4_red', models.CharField(default='100', max_length=64, verbose_name='pixel_4_red')),
                ('pixel_4_green', models.CharField(default='100', max_length=64, verbose_name='pixel_4_green')),
                ('pixel_4_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_4_blue')),
                ('pixel_5_red', models.CharField(default='100', max_length=64, verbose_name='pixel_5_red')),
                ('pixel_5_green', models.CharField(default='100', max_length=64, verbose_name='pixel_5_green')),
                ('pixel_5_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_5_blue')),
                ('pixel_6_red', models.CharField(default='100', max_length=64, verbose_name='pixel_6_red')),
                ('pixel_6_green', models.CharField(default='100', max_length=64, verbose_name='pixel_6_green')),
                ('pixel_6_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_6_blue')),
                ('pixel_7_red', models.CharField(default='100', max_length=64, verbose_name='pixel_7_red')),
                ('pixel_7_green', models.CharField(default='100', max_length=64, verbose_name='pixel_7_green')),
                ('pixel_7_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_7_blue')),
                ('pixel_8_red', models.CharField(default='100', max_length=64, verbose_name='pixel_8_red')),
                ('pixel_8_green', models.CharField(default='100', max_length=64, verbose_name='pixel_8_green')),
                ('pixel_8_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_8_blue')),
                ('pixel_9_red', models.CharField(default='100', max_length=64, verbose_name='pixel_9_red')),
                ('pixel_9_green', models.CharField(default='100', max_length=64, verbose_name='pixel_9_green')),
                ('pixel_9_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_9_blue')),
                ('pixel_10_red', models.CharField(default='100', max_length=64, verbose_name='pixel_10_red')),
                ('pixel_10_green', models.CharField(default='100', max_length=64, verbose_name='pixel_10_green')),
                ('pixel_10_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_10_blue')),
                ('pixel_11_red', models.CharField(default='100', max_length=64, verbose_name='pixel_11_red')),
                ('pixel_11_green', models.CharField(default='100', max_length=64, verbose_name='pixel_11_green')),
                ('pixel_11_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_11_blue')),
                ('pixel_12_red', models.CharField(default='100', max_length=64, verbose_name='pixel_12_red')),
                ('pixel_12_green', models.CharField(default='100', max_length=64, verbose_name='pixel_12_green')),
                ('pixel_12_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_12_blue')),
                ('pixel_13_red', models.CharField(default='100', max_length=64, verbose_name='pixel_13_red')),
                ('pixel_13_green', models.CharField(default='100', max_length=64, verbose_name='pixel_13_green')),
                ('pixel_13_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_13_blue')),
                ('pixel_14_red', models.CharField(default='100', max_length=64, verbose_name='pixel_14_red')),
                ('pixel_14_green', models.CharField(default='100', max_length=64, verbose_name='pixel_14_green')),
                ('pixel_14_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_14_blue')),
                ('pixel_15_red', models.CharField(default='100', max_length=64, verbose_name='pixel_15_red')),
                ('pixel_15_green', models.CharField(default='100', max_length=64, verbose_name='pixel_15_green')),
                ('pixel_15_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_15_blue')),
                ('pixel_16_red', models.CharField(default='100', max_length=64, verbose_name='pixel_16_red')),
                ('pixel_16_green', models.CharField(default='100', max_length=64, verbose_name='pixel_16_green')),
                ('pixel_16_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_16_blue')),
                ('pixel_17_red', models.CharField(default='100', max_length=64, verbose_name='pixel_17_red')),
                ('pixel_17_green', models.CharField(default='100', max_length=64, verbose_name='pixel_17_green')),
                ('pixel_17_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_17_blue')),
                ('pixel_18_red', models.CharField(default='100', max_length=64, verbose_name='pixel_18_red')),
                ('pixel_18_green', models.CharField(default='100', max_length=64, verbose_name='pixel_18_green')),
                ('pixel_18_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_18_blue')),
                ('pixel_19_red', models.CharField(default='100', max_length=64, verbose_name='pixel_19_red')),
                ('pixel_19_green', models.CharField(default='100', max_length=64, verbose_name='pixel_19_green')),
                ('pixel_19_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_19_blue')),
                ('pixel_20_red', models.CharField(default='100', max_length=64, verbose_name='pixel_20_red')),
                ('pixel_20_green', models.CharField(default='100', max_length=64, verbose_name='pixel_20_green')),
                ('pixel_20_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_20_blue')),
                ('pixel_21_red', models.CharField(default='100', max_length=64, verbose_name='pixel_21_red')),
                ('pixel_21_green', models.CharField(default='100', max_length=64, verbose_name='pixel_21_green')),
                ('pixel_21_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_21_blue')),
                ('pixel_22_red', models.CharField(default='100', max_length=64, verbose_name='pixel_22_red')),
                ('pixel_22_green', models.CharField(default='100', max_length=64, verbose_name='pixel_22_green')),
                ('pixel_22_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_22_blue')),
                ('pixel_23_red', models.CharField(default='100', max_length=64, verbose_name='pixel_23_red')),
                ('pixel_23_green', models.CharField(default='100', max_length=64, verbose_name='pixel_23_green')),
                ('pixel_23_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_23_blue')),
                ('pixel_24_red', models.CharField(default='100', max_length=64, verbose_name='pixel_24_red')),
                ('pixel_24_green', models.CharField(default='100', max_length=64, verbose_name='pixel_24_green')),
                ('pixel_24_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_24_blue')),
                ('pixel_25_red', models.CharField(default='100', max_length=64, verbose_name='pixel_25_red')),
                ('pixel_25_green', models.CharField(default='100', max_length=64, verbose_name='pixel_25_green')),
                ('pixel_25_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_25_blue')),
                ('pixel_26_red', models.CharField(default='100', max_length=64, verbose_name='pixel_26_red')),
                ('pixel_26_green', models.CharField(default='100', max_length=64, verbose_name='pixel_26_green')),
                ('pixel_26_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_26_blue')),
                ('pixel_27_red', models.CharField(default='100', max_length=64, verbose_name='pixel_27_red')),
                ('pixel_27_green', models.CharField(default='100', max_length=64, verbose_name='pixel_27_green')),
                ('pixel_27_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_27_blue')),
                ('pixel_28_red', models.CharField(default='100', max_length=64, verbose_name='pixel_28_red')),
                ('pixel_28_green', models.CharField(default='100', max_length=64, verbose_name='pixel_28_green')),
                ('pixel_28_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_28_blue')),
                ('pixel_29_red', models.CharField(default='100', max_length=64, verbose_name='pixel_29_red')),
                ('pixel_29_green', models.CharField(default='100', max_length=64, verbose_name='pixel_29_green')),
                ('pixel_29_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_29_blue')),
                ('pixel_30_red', models.CharField(default='100', max_length=64, verbose_name='pixel_30_red')),
                ('pixel_30_green', models.CharField(default='100', max_length=64, verbose_name='pixel_30_green')),
                ('pixel_30_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_30_blue')),
                ('Script_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Script_2', to='lamps.scripts')),
            ],
        ),
        migrations.CreateModel(
            name='Script_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pixel_1_red', models.CharField(default='100', max_length=64, verbose_name='pixel_1_red')),
                ('pixel_1_green', models.CharField(default='100', max_length=64, verbose_name='pixel_1_green')),
                ('pixel_1_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_1_blue')),
                ('pixel_2_red', models.CharField(default='100', max_length=64, verbose_name='pixel_2_red')),
                ('pixel_2_green', models.CharField(default='100', max_length=64, verbose_name='pixel_2_green')),
                ('pixel_2_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_2_blue')),
                ('pixel_3_red', models.CharField(default='100', max_length=64, verbose_name='pixel_3_red')),
                ('pixel_3_green', models.CharField(default='100', max_length=64, verbose_name='pixel_3_green')),
                ('pixel_3_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_3_blue')),
                ('pixel_4_red', models.CharField(default='100', max_length=64, verbose_name='pixel_4_red')),
                ('pixel_4_green', models.CharField(default='100', max_length=64, verbose_name='pixel_4_green')),
                ('pixel_4_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_4_blue')),
                ('pixel_5_red', models.CharField(default='100', max_length=64, verbose_name='pixel_5_red')),
                ('pixel_5_green', models.CharField(default='100', max_length=64, verbose_name='pixel_5_green')),
                ('pixel_5_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_5_blue')),
                ('pixel_6_red', models.CharField(default='100', max_length=64, verbose_name='pixel_6_red')),
                ('pixel_6_green', models.CharField(default='100', max_length=64, verbose_name='pixel_6_green')),
                ('pixel_6_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_6_blue')),
                ('pixel_7_red', models.CharField(default='100', max_length=64, verbose_name='pixel_7_red')),
                ('pixel_7_green', models.CharField(default='100', max_length=64, verbose_name='pixel_7_green')),
                ('pixel_7_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_7_blue')),
                ('pixel_8_red', models.CharField(default='100', max_length=64, verbose_name='pixel_8_red')),
                ('pixel_8_green', models.CharField(default='100', max_length=64, verbose_name='pixel_8_green')),
                ('pixel_8_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_8_blue')),
                ('pixel_9_red', models.CharField(default='100', max_length=64, verbose_name='pixel_9_red')),
                ('pixel_9_green', models.CharField(default='100', max_length=64, verbose_name='pixel_9_green')),
                ('pixel_9_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_9_blue')),
                ('pixel_10_red', models.CharField(default='100', max_length=64, verbose_name='pixel_10_red')),
                ('pixel_10_green', models.CharField(default='100', max_length=64, verbose_name='pixel_10_green')),
                ('pixel_10_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_10_blue')),
                ('pixel_11_red', models.CharField(default='100', max_length=64, verbose_name='pixel_11_red')),
                ('pixel_11_green', models.CharField(default='100', max_length=64, verbose_name='pixel_11_green')),
                ('pixel_11_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_11_blue')),
                ('pixel_12_red', models.CharField(default='100', max_length=64, verbose_name='pixel_12_red')),
                ('pixel_12_green', models.CharField(default='100', max_length=64, verbose_name='pixel_12_green')),
                ('pixel_12_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_12_blue')),
                ('pixel_13_red', models.CharField(default='100', max_length=64, verbose_name='pixel_13_red')),
                ('pixel_13_green', models.CharField(default='100', max_length=64, verbose_name='pixel_13_green')),
                ('pixel_13_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_13_blue')),
                ('pixel_14_red', models.CharField(default='100', max_length=64, verbose_name='pixel_14_red')),
                ('pixel_14_green', models.CharField(default='100', max_length=64, verbose_name='pixel_14_green')),
                ('pixel_14_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_14_blue')),
                ('pixel_15_red', models.CharField(default='100', max_length=64, verbose_name='pixel_15_red')),
                ('pixel_15_green', models.CharField(default='100', max_length=64, verbose_name='pixel_15_green')),
                ('pixel_15_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_15_blue')),
                ('pixel_16_red', models.CharField(default='100', max_length=64, verbose_name='pixel_16_red')),
                ('pixel_16_green', models.CharField(default='100', max_length=64, verbose_name='pixel_16_green')),
                ('pixel_16_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_16_blue')),
                ('pixel_17_red', models.CharField(default='100', max_length=64, verbose_name='pixel_17_red')),
                ('pixel_17_green', models.CharField(default='100', max_length=64, verbose_name='pixel_17_green')),
                ('pixel_17_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_17_blue')),
                ('pixel_18_red', models.CharField(default='100', max_length=64, verbose_name='pixel_18_red')),
                ('pixel_18_green', models.CharField(default='100', max_length=64, verbose_name='pixel_18_green')),
                ('pixel_18_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_18_blue')),
                ('pixel_19_red', models.CharField(default='100', max_length=64, verbose_name='pixel_19_red')),
                ('pixel_19_green', models.CharField(default='100', max_length=64, verbose_name='pixel_19_green')),
                ('pixel_19_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_19_blue')),
                ('pixel_20_red', models.CharField(default='100', max_length=64, verbose_name='pixel_20_red')),
                ('pixel_20_green', models.CharField(default='100', max_length=64, verbose_name='pixel_20_green')),
                ('pixel_20_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_20_blue')),
                ('pixel_21_red', models.CharField(default='100', max_length=64, verbose_name='pixel_21_red')),
                ('pixel_21_green', models.CharField(default='100', max_length=64, verbose_name='pixel_21_green')),
                ('pixel_21_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_21_blue')),
                ('pixel_22_red', models.CharField(default='100', max_length=64, verbose_name='pixel_22_red')),
                ('pixel_22_green', models.CharField(default='100', max_length=64, verbose_name='pixel_22_green')),
                ('pixel_22_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_22_blue')),
                ('pixel_23_red', models.CharField(default='100', max_length=64, verbose_name='pixel_23_red')),
                ('pixel_23_green', models.CharField(default='100', max_length=64, verbose_name='pixel_23_green')),
                ('pixel_23_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_23_blue')),
                ('pixel_24_red', models.CharField(default='100', max_length=64, verbose_name='pixel_24_red')),
                ('pixel_24_green', models.CharField(default='100', max_length=64, verbose_name='pixel_24_green')),
                ('pixel_24_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_24_blue')),
                ('pixel_25_red', models.CharField(default='100', max_length=64, verbose_name='pixel_25_red')),
                ('pixel_25_green', models.CharField(default='100', max_length=64, verbose_name='pixel_25_green')),
                ('pixel_25_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_25_blue')),
                ('pixel_26_red', models.CharField(default='100', max_length=64, verbose_name='pixel_26_red')),
                ('pixel_26_green', models.CharField(default='100', max_length=64, verbose_name='pixel_26_green')),
                ('pixel_26_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_26_blue')),
                ('pixel_27_red', models.CharField(default='100', max_length=64, verbose_name='pixel_27_red')),
                ('pixel_27_green', models.CharField(default='100', max_length=64, verbose_name='pixel_27_green')),
                ('pixel_27_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_27_blue')),
                ('pixel_28_red', models.CharField(default='100', max_length=64, verbose_name='pixel_28_red')),
                ('pixel_28_green', models.CharField(default='100', max_length=64, verbose_name='pixel_28_green')),
                ('pixel_28_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_28_blue')),
                ('pixel_29_red', models.CharField(default='100', max_length=64, verbose_name='pixel_29_red')),
                ('pixel_29_green', models.CharField(default='100', max_length=64, verbose_name='pixel_29_green')),
                ('pixel_29_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_29_blue')),
                ('pixel_30_red', models.CharField(default='100', max_length=64, verbose_name='pixel_30_red')),
                ('pixel_30_green', models.CharField(default='100', max_length=64, verbose_name='pixel_30_green')),
                ('pixel_30_blue', models.CharField(default='100', max_length=64, verbose_name='pixel_30_blue')),
                ('Script_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Script_1', to='lamps.scripts')),
            ],
        ),
        migrations.CreateModel(
            name='Humidity_Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Humidity', models.CharField(default='1', max_length=64, verbose_name='Humidity')),
                ('Temperature', models.CharField(default='1', max_length=64, verbose_name='Temperature')),
                ('H_T', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='H_T', to='lamps.lamps')),
            ],
        ),
    ]