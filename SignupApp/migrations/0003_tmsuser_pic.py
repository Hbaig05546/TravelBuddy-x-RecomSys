# Generated by Django 3.2.6 on 2021-10-14 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignupApp', '0002_alter_tmsuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmsuser',
            name='pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]