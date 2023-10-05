from django.urls import path
from .views import get_employee, CustomAuthToken, create_employee, get_user
from .views import hello_world3


urlpatterns = [

    # Token generation and retreval of authenticated user details
    path('api/token/', CustomAuthToken.as_view(), name='get-auth-token'),

    # Path to be used to get the details of authenticated user (without token)
    path('api/get-user/', get_user, name='get-employee'),

    # Path to be used to get the employee details
    path('api/get-employee/', get_employee, name='get-employee'),

    # Path to be used to add new employee details
    path('api/create-employee/', create_employee, name='create-employee'),

    path('hello-world3/', hello_world3, name='hello-world3'),

]
