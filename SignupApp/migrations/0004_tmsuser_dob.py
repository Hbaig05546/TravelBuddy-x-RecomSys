# Generated by Django 3.2.6 on 2021-10-17 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SignupApp', '0003_tmsuser_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmsuser',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
