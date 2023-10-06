from django.db import models

# Employee Event


class Profile(models.Model):
    employee = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    mobile_no = models.CharField(max_length=15, null=False)
    designation = models.CharField(max_length=20, null=False)
    department = models.CharField(max_length=20, null=False)
    reporting_manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='manager_name'
    )

    # Role field with a check constraint
    ROLE_CHOICES = (
        ('Trainee', 'Trainee'),
        ('Associate', 'Associate'),
        ('Consultant', 'Consultant'),
        ('Senior Associate', 'Senior Associate'),
        ('Manager', 'Manager'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        null=False,
    )

    DEPARTMENT_CHOICES = (
        ('SAC', 'SAC'),
        ('Engineering', 'Engineering'),
        ('SAP SD', 'SAP SD'),
        ('SAP PP', 'SAP PP'),
        ('SAP MM', 'SAP MM'),
        ('SAP FICO', 'SAP FICO'),
        ('SAP ABAP', 'SAP ABAP'),
    )

    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES,
        null=False,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
