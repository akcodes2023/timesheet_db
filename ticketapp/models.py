# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
from django.db import models
# from projectapp.models import Project 

# from timesheetapp.models import Project


# project_instance = Project.objects.create(project="Deesan")


# Create your models here.
class Ticket(models.Model):
    ticket = models.AutoField(primary_key=True)
    ticket_description = models.CharField(max_length=250, null=False)
    project = models.ForeignKey('projectapp.Project', on_delete=models.CASCADE)
    '''
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    project_object = GenericForeignKey('content_type', 'object_id')
    '''
    reporter_name = models.CharField(max_length=100, null=False)
    reporter_email = models.CharField(max_length=100, null=False)
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
        null=False,
    )

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

    # module = models.ForeignKey(Module, on_delete=models.CASCADE)

    MODULE_CHOICES = (
        ('SAP SD', 'SAP SD'),
        ('SAP PP', 'SAP PP'),
        ('SAP MM', 'SAP MM'),
        ('SAP FICO', 'SAP FICO'),
        ('SAP ABAP', 'SAP ABAP'),
    )

    module = models.CharField(
        max_length=20,
        choices=MODULE_CHOICES,
        null=False,
    )

    def __str__(self):
        return f"Ticket #{self.ticket}"


class Meta:
    constraints = [
            models.CheckConstraint(
                check=models.Q(priority__in=['Low',
                                             'Medium',
                                             'High',
                                             'Show Stopper']),
                name='valid_priority_check',
            ),
            models.CheckConstraint(
                check=models.Q(category__in=['Technical',
                                             'Functional',
                                             'Error Messages',
                                             'Reporting, Analytics and Forms',
                                             'Custom Development']),
                name='valid_category_check',
            ),
            models.CheckConstraint(
                check=models.Q(module__in=['SAP SD',
                                           'SAP PP',
                                           'SAP MM',
                                           'SAP FICO',
                                           'SAP ABAP']),
                name='valid_module_check',
            ),
    ]
