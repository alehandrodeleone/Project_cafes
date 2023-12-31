# Generated by Django 4.2.3 on 2023-08-17 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0022_alter_restaurant_owner_cafe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='owner_cafe',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='res', to=settings.AUTH_USER_MODEL),
        ),
    ]
