# Generated by Django 4.0.1 on 2022-04-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookTicketApp', '0005_alter_packagedetails_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedetails',
            name='pTitle',
            field=models.CharField(blank=True, default='N.A.', max_length=25, null=True),
        ),
    ]
