# Generated by Django 4.2.5 on 2023-10-04 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='User',
        ),
    ]
