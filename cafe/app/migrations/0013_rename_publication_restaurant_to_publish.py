# Generated by Django 4.2.3 on 2023-08-09 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_restaurant_publication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='publication',
            new_name='to_publish',
        ),
    ]
