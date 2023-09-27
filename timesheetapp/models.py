from django.utils import timezone
from typing import Any
from django.db import models
from django.db.models import Q

# Create your models here.

# Project
#  Model/Table
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
    


class Module(models.Model):
     module = models.CharField(max_length=250, null=False)
     module_description = models.CharField(max_length=250, null=False)

     def __str__(self):
        return self.module
    

class Ticket(models.Model):
    ticket = models.AutoField(primary_key=True)
    ticket_description = models.CharField(max_length=250, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reporter = models.CharField(max_length=100, null=False)
    reporter_contact = models.CharField(max_length=10, null=False)

    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Show Stopper', 'Show Stopper'),
    )

    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        # unique=True,
        null=False,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['priority'],
                name='unique_priority',
            ),
            models.CheckConstraint(
                check=models.Q(priority__in=['Low', 'Medium', 'High', 'Show Stopper']),
                name='valid_priority_check',
            ),
        ]
    
    # Service type (For now only 2 type of service is included)
    CATEGORY_CHOICES = (
        ('Technical', 'Technical'),
        ('Functional', 'Functional'),
        ('Error Messages', 'Error Messages'),
        ('Reporting, Analytics and Forms', 'Reporting, Analytics and Forms'),
        ('Custom Development', 'Custom Development'),
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        # unique=True,
        null=False,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['category'],
                name='unique_category',
            ),
            models.CheckConstraint(
                check=models.Q(category__in=['Technical', 'Functional', 'Error Messages', 'Reporting, Analytics and Forms','Custom Development']),
                name='valid_category_check',
            ),
        ]

    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket #{self.ticket}"
    

'''
    SAPMODULE_CHOICES = (
        ('SAP SD', 'SAP SD'),
        ('SAP PP', 'SAP PP'),
        ('SAP MM', 'SAP MM'),
        ('SAP FICO', 'SAP FICO'),
        ('SAP ABAP', 'SAP ABAP'),
    )

    module = models.CharField(
        max_length=50,
        choices=SAPMODULE_CHOICES,
        # unique=True,
        null=False,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['module'],
                name='unique_module',
            ),
           models.CheckConstraint(
                check=models.Q(module__in=['SAP SD', 'SAP PP', 'SAP MM', 'SAP FICO', 'SAP ABAP']),
                name='valid_module_check',
            ),
        ]

    '''    

class Timesheet(models.Model):
        # week
        timesheet = models.AutoField(primary_key=True)
        date = models.DateField(null=True)
        project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
        ticket = models.ForeignKey(
            Ticket, 
            on_delete=models.CASCADE, 
            to_field='ticket',
            null=False, 
            related_name='your_ticket'
            )
        

        '''
        module = models.ForeignKey(
            Ticket,
            on_delete=models.CASCADE, 
            #to_field='module', 
            null=False, 
            related_name='your_module'
            )
        
        
        category = models.ForeignKey(
            Ticket, 
            on_delete=models.CASCADE, 
            to_field='category', 
            null=False, 
            related_name='your_category'
            )
        '''

        starttime = models.DateTimeField(null=False)
        endtime = models.DateTimeField(null=False)
        effort_description = models.CharField(max_length=250,null=False)

        def __str__(self):
            return f"{self.timesheet}"