# Generated by Django 4.2.3 on 2023-08-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_restaurant_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
