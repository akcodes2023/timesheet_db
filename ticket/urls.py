# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('ticket/', views.hello_world2, name='hello_world2'),
]
