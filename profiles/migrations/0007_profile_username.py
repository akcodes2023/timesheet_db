# Generated by Django 4.2.5 on 2023-10-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_remove_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
