# Generated by Django 3.1.7 on 2021-03-28 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lamps', '0002_programlamps1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programlamps1',
            old_name='pixel_1b',
            new_name='pixel_1_blue',
        ),
        migrations.RenameField(
            model_name='programlamps1',
            old_name='pixel_1g',
            new_name='pixel_1_green',
        ),
        migrations.RenameField(
            model_name='programlamps1',
            old_name='pixel_1r',
            new_name='pixel_1_red',
        ),
    ]
