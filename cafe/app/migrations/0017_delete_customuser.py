# Generated by Django 4.2.3 on 2023-08-11 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]