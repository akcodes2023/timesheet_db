from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

# Employee Event


class Profile(models.Model):
    employee = models.AutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    mobile_no = models.CharField(max_length=15, null=False)
    designation = models.CharField(max_length=20, null=False)
    # department = models.CharField(max_length=20, null=False)
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

    def save(self, *args, **kwargs):
        # Check if this is a new Profile instance
        if not hasattr(self, 'user'):
            # Check if the username already exists
            if User.objects.filter(username=self.username).exists():
                raise ValidationError("Username already exists. Please choose a different username.")

            # Create a User profile corresponding to the Profile instance
            user = User(username=self.username)
            # Update user fields as needed
            user.first_name = self.first_name
            user.last_name = self.last_name
            user.email = self.email
            user.save()

        # Call the parent class's save method to save the Profile instance
        super(Profile, self).save(*args, **kwargs)
