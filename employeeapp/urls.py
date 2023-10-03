# from django.contrib import admin
from django.urls import path
from . import views

# For TokenAuthentication
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('employeeapp/', views.hello_world3, name='hello_world3'),
    path('api/employees/get-employee/', views.get_employee, name='get-employee'),
    path('api/employees/create-employee/', views.create_employee, name='create-employee'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
