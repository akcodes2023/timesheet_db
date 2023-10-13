# from datetime import timezone
from django.db import models
from django.utils import timezone


class Worklog(models.Model):
    # week
    worklog = models.AutoField(primary_key=True)
    # event_date = models.DateField(default=timezone.now().date())
    user = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        null=False
        )

    title = models.CharField(max_length=20, null=False)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        null=False
        )

    ticket = models.ForeignKey(
        'ticket.Ticket',
        on_delete=models.CASCADE,
        # to_field='ticket',
        null=False,
        related_name='your_ticket'
        )

    description = models.TextField()
    # description = models.CharField(max_length=250, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    """
    start_date = models.DateTimeField(
        null=False,
        # blank=True,
        default=timezone.now
        )

    end_date = models.DateTimeField(
        null=False,
        # blank=True,
        default=timezone.now
        )
    """

    def __str__(self):
        return f"Worklog #{self.worklog}"


"""

class Worklog(models.Model):
    # week
    worklog = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    starttime = models.TimeField(null=False)
    # endtime = models.TimeField(null=True, blank=True,)
    endtime = models.TimeField(null=False)
    title = models.CharField(max_length=20, null=False)
    raised_by = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        null=False
        )

    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        null=False
        )

    ticket = models.ForeignKey(
        'ticket.Ticket',
        on_delete=models.CASCADE,
        # to_field='ticket',
        null=False,
        related_name='your_ticket'
        )

    effort_description = models.CharField(max_length=250, null=False)

    APPROVALSTATUS_CHOICES = (
        ('Submitted', 'Submitted'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    status = models.CharField(
        max_length=20,
        choices=APPROVALSTATUS_CHOICES,
        null=False,
        default='Submitted',
    )

    def __str__(self):
        return f"Worklog #{self.worklog}"


"""