# Generated by Django 4.2.3 on 2023-08-18 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
