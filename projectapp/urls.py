# from django.contrib import admin
from django.urls import path
from . import views

# For TokenAuthentication
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('projectapp/', views.hello_world4, name='hello_world2'),
    path('api/project/get-project/', views.get_project, name='get-project'),
    path('api/project/create-project/', views.create_project, name='create-project'),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
