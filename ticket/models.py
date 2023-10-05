from django.db import models


# Create your models here.
class Ticket(models.Model):
    ticket = models.AutoField(primary_key=True)
    ticket_description = models.CharField(max_length=250, null=False)
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)
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
