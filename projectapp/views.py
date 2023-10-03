# from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.decorators import api_view, permission_classes  # authentication_classes,
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer
from projectapp.models import Project


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project(request):
    if request.method == 'GET':
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):

    if request.method == 'POST':
        # Handle POST request to create a new employee
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        return Response(serializer.errors, status=400)  # 400 Bad Request

# Create your views here.


def hello_world4(request):
    return HttpResponse("Hello, World4!")
