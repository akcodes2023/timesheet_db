# Generated by Django 4.2.5 on 2023-10-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetapp', '0013_timesheet_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='endtime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='starttime',
            field=models.TimeField(),
        ),
    ]