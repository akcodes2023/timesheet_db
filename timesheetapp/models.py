from django.db import models
from django.core.exceptions import ValidationError

# from ticketapp.models import Ticket
# from django.db.models import Q

# Create your models here.

# Timesheet Model/Table


class Timesheet(models.Model):
    # week
    timesheet = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    starttime = models.TimeField(null=False)
    endtime = models.TimeField(null=False)
    title = approval_status = models.CharField(default="", max_length=20, null=False)
    raised_by = models.ForeignKey('employeeapp.Employee', on_delete=models.CASCADE, null=False)
    # project = models.ForeignKey('projectapp.Project', on_delete=models.CASCADE, null=False)
    ticket = models.ForeignKey(
        'ticketapp.Ticket',
        on_delete=models.CASCADE,
        # to_field='ticket',
        null=False,
        related_name='your_ticket'
        )

    effort_description = models.CharField(max_length=250, null=False)

    APPROVALSTATUS_CHOICES = (
        ('', ''),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    approval_status = models.CharField(
        max_length=20,
        choices=APPROVALSTATUS_CHOICES,
        null=False,
        default="",
    )

    def clean(self):
        # Check if a timesheet already exists for the same project, ticket, and date
        existing_timesheets = Timesheet.objects.filter(
            project=self.project,
            ticket=self.ticket,
            date=self.date
        )

        # Exclude the current timesheet instance if it's being edited
        if self.pk:
            existing_timesheets = existing_timesheets.exclude(pk=self.pk)

        if existing_timesheets.exists():
            raise ValidationError("A timesheet for this project and ticket already exists for this date.")

    def __str__(self):
        return f"Timesheet #{self.timesheet}"


'''
    BILLABLESTATUS_CHOICES = (
        ('Billable', 'Billable'),
        ('Non Billable', 'Non Billable'),
    )

    billable_status = models.CharField(
        max_length=20,
        choices=BILLABLESTATUS_CHOICES,
        null=False,
        default="Billable",
    )


Total hours
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def calculate_total_hours(self):
        if self.starttime and self.endtime:
            time_difference = self.endtime - self.starttime
            total_seconds = time_difference.total_seconds()
            total_hours = total_seconds / 3600  # 3600 seconds in an hour
            self.total_hours = round(total_hours, 2)  # Round to 2 decimal places
        else:
            self.total_hours = None

    def save(self, *args, **kwargs):
        self.calculate_total_hours()  # Calculate total hours before saving
        super().save(*args, **kwargs)  # Call the original save method


class Dispute(models.Model):
    dispute = models.AutoField(primary_key=True)
    timesheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=250, null=False)
    attachement = models.FileField(upload_to='Dispute_Documents/')  # Use FileField for documents

    DISPUTESTATUS_CHOICES = (
        ('Created', 'Created'),
        ('In Review', 'In Review'),
        ('Dispute Approved', 'Dispute Approved'),
        ('Dispute Partially Approved', 'Dispute Partially Approved'),
        ('Dispute Rejected', 'Dispute Rejected'),
    )

    dispute_status = models.CharField(
        max_length=50,
        choices=DISPUTESTATUS_CHOICES,
        null=False,
        default="Created",
    )

    def __str__(self):
        return f"Dispute #{self.dispute}"

'''


class Meta:
    constraints = [
            models.CheckConstraint(
                check=models.Q(approval_status__in=['',
                                                    'Approved',
                                                    'Rejected',
                                                    ]),
                name='valid_approval_status_check',
            ),
            '''
            models.CheckConstraint(
                check=models.Q(billable_status__in=['Bilable',
                                                    'Non Billable']),
                name='valid_billable_status_check',
            ),
            '''
        ]
