# Generated by Django 4.2.5 on 2023-10-06 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0003_worklog_delete_timesheet'),
        ('profiles', '0003_user_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
