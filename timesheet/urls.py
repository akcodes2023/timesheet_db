# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.hello_world,
        name='hello_world'
        ),

    path(
        'api/employees/get-timesheet/',
        views.get_timesheet,
        name='get-timesheet'
        ),

    path(
        'api/employees/create-timesheet/',
        views.create_timesheet,
        name='create-timesheet'
        ),

    # API path to get the timesheet details of the employee based on the
    # selected date range
    path(
        'api/employees/events/filter/',
        views.get_timesheet_bydate_range,
        name='create-timesheet'
        ),

    # API path to get the timesheet details of the employee based on the
    # selected date and approval_status
    path(
        'api/timesheet/date/',
        views.get_timesheet_bydate,
        name='get_timesheet_date'
        ),

    # API path to get the timesheet and profile details of the employee
    # who have not submitted the timesheet for the selected date
    path(
        'api/timesheet/not_submitted/',
        views.timesheet_not_submitted,
        name='get_timesheet_date'
        ),

]
