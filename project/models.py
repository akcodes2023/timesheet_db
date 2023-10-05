from django.db import models


# Project Model/Table


class Project(models.Model):
    project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=250, null=False)
    startdate = models.DateField(null=False)
    enddate = models.DateField(null=True, default=None)

    # Service type (For now only 2 type of service is included)
    PROJECTTYPE_CHOICES = (
        ('SAP Implementation', 'SAP Implementation'),
        ('SAP Support and Maintenance', 'SAP Support and Maintenance'),
    )

    project_type = models.CharField(
        max_length=50,
        choices=PROJECTTYPE_CHOICES,
        null=False,
    )

    def __str__(self):
        return self.project_name
