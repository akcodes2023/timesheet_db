from django.db import models


class Worklog(models.Model):
    # week
    worklog = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    starttime = models.TimeField(null=False)
    endtime = models.TimeField(null=True, blank=True,)
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
