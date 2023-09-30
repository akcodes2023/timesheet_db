# Generated by Django 4.2.5 on 2023-09-30 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetapp', '0005_timesheet_billable_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispute',
            fields=[
                ('dispute', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=250)),
                ('attachement', models.FileField(upload_to='Dispute_Documents/')),
                ('dispute_status', models.CharField(choices=[('Created', 'Created'), ('In Review', 'In Review'), ('Dispute Approved', 'Dispute Approved'), ('Dispute Partially Approved', 'Dispute Partially Approved'), ('Dispute Rejected', 'Dispute Rejected')], default='Created', max_length=50)),
                ('timesheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheetapp.timesheet')),
            ],
        ),
    ]
