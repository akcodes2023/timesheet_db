# Generated by Django 4.2.5 on 2023-10-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.CharField(max_length=250)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField(default=None, null=True)),
                ('project_type', models.CharField(choices=[('SAP Implementation', 'SAP Implementation'), ('SAP Support and Maintenance', 'SAP Support and Maintenance')], max_length=50)),
            ],
        ),
    ]
