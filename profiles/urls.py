from django.urls import path
from .views import get_employee, create_employee, get_user, CustomAuthToken
from .views import hello_world3

# For TokenAuthentication
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    # path('api/token/', custom_auth_token, name='get-auth-token'),
    path('api/token/', CustomAuthToken.as_view(), name='get-auth-token'),
    # path('api/token/', obtain_auth_token, name='get-auth-token'),
    path(
        'api/get/authenticated-user/',
        get_user,
        name='get-user-by-id'
        ),

    path('api/get-employee/', get_employee, name='get-employee'),
    path('api/create-employee/', create_employee, name='create-employee'),
    path('hello-world3/', hello_world3, name='hello-world3'),

]
