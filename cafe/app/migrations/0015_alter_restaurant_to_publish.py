# Generated by Django 4.2.3 on 2023-08-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_restaurant_to_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='to_publish',
            field=models.BooleanField(default=False),
        ),
    ]
