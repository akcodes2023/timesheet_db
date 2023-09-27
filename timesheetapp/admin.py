from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Project)
admin.site.register(Ticket)
admin.site.register(Timesheet)
admin.site.register(Module)