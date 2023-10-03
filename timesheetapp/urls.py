# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('api/employees/get-timesheet/', views.get_timesheet, name='get-timesheet'),
    path('api/employees/create-timesheet/', views.create_timesheet, name='create-timesheet'),
]
