# Generated by Django 4.0.1 on 2022-04-18 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookTicketApp', '0006_alter_packagedetails_ptitle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PackageDetails',
            new_name='PackageDetail',
        ),
    ]
