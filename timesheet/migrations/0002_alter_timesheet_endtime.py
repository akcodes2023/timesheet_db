# Generated by Django 4.2.5 on 2023-10-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='endtime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
