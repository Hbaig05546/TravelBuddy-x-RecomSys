# Generated by Django 3.2.6 on 2021-10-20 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignupApp', '0008_alter_tmsuser_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmsuser',
            name='mobileno',
            field=models.CharField(max_length=12),
        ),
    ]
