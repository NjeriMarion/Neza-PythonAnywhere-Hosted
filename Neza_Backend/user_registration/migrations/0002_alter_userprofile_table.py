# Generated by Django 4.2.5 on 2023-09-09 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='user_registration_userprofile',
        ),
    ]