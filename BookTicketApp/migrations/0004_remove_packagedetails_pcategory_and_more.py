# Generated by Django 4.0.1 on 2022-04-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookTicketApp', '0003_alter_packagedetails_pcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagedetails',
            name='PCategory',
        ),
        migrations.AddField(
            model_name='packagedetails',
            name='pCategory',
            field=models.TextField(blank=True, default='no category provided !', max_length=518),
        ),
        migrations.AlterField(
            model_name='packagedetails',
            name='pdetails',
            field=models.TextField(blank=True, default='no details provided !', max_length=518),
        ),
    ]
