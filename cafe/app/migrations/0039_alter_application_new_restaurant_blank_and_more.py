# Generated by Django 4.2.3 on 2023-08-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_application_new_restaurant_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_new_restaurant',
            name='blank',
            field=models.FileField(null=True, upload_to='documents_owner/'),
        ),
        migrations.AlterField(
            model_name='application_new_restaurant',
            name='document1',
            field=models.FileField(null=True, upload_to='documents_owner/'),
        ),
        migrations.AlterField(
            model_name='application_new_restaurant',
            name='document2',
            field=models.FileField(null=True, upload_to='documents_owner/'),
        ),
        migrations.AlterField(
            model_name='application_new_restaurant',
            name='document3',
            field=models.FileField(null=True, upload_to='documents_owner/'),
        ),
    ]
