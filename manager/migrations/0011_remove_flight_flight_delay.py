# Generated by Django 3.2 on 2021-05-05 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_auto_20210504_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_delay',
        ),
    ]
