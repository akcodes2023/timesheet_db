# from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes  # authentication_classes,
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer
from employeeapp.models import Employee


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_employee(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_employee(request):

    if request.method == 'POST':
        '''
        # print(type(request.data))
        '''
        # Handle POST request to create a new employee
        serializer = EmployeeSerializer(data=request.data)
        '''
        # print(type(serializer))
        # print(serializer.initial_data)
        '''
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        return Response(serializer.errors, status=400)  # 400 Bad Request

# Create your views here.


def hello_world3(request):
    return HttpResponse("Hello, World3!")
