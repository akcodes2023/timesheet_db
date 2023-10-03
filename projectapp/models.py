from django.db import models

'''
# from ticketapp.models import Ticket
# from django.db.models import Q
'''

# Create your models here.

# Project Model/Table


class Project(models.Model):
    project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)

    '''
    project_description = models.CharField(max_length=250, null=False)
    client_name = models.CharField(max_length=50, null=False)
    client_manager = models.CharField(max_length=50, null=False)
    client_contact = models.CharField(max_length=50, null=False)
    client_email = models.EmailField(max_length=254, null=False)
    project_manager = models.CharField(max_length=50, null=False)
    project_manager_contact = models.CharField(max_length=50, null=False)
    project_manager_email = models.EmailField(max_length=254, null=False)
    # startdate = models.DateField(default=timezone.now, null=False)
    # enddate = models.DateField(null=True)


    # status field with Active or Inactive status
    ACTIVE_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]

    status = models.BooleanField(
        default=True,  # Set the default status to Active
        choices=ACTIVE_CHOICES,
    )

    # Service type (For now only 2 type of service is included)
    SERVICE_CHOICES = (
        ('SAP Implementation', 'SAP Implementation'),
        ('SAP Support and Maintenance', 'SAP Support and Maintenance'),
    )
    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        unique=True,
        null=False,
    )


    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(service_type__in=['SAP Implementation', 'SAP Support and Maintenance']),
                name='valid_service_check',
            )
        ]

    '''

    def __str__(self):
        return self.project_name
