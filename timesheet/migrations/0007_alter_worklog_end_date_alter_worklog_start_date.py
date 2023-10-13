# Generated by Django 4.2.5 on 2023-10-13 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0006_rename_effort_description_worklog_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='worklog',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
