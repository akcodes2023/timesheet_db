from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfilesSerializer, UsersSerializer


'''
from profiles.models import User
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_employee(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = ProfilesSerializer(user, many=True)
        return Response(serializer.data)
'''


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    if request.method == 'GET':
        user = request.user

        # You can directly access the authenticated user's data
        userserializer = UsersSerializer(user)
        return Response(userserializer.data)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            token = Token.objects.get(key=response.data['token'])
            user = token.user
            serializer = UsersSerializer(user)
            data = {'token': token.key, 'user_details': serializer.data}
            return Response(data)
        return response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_employee(request):
    if request.method == 'POST':
        serializer = ProfilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        return Response(serializer.errors, status=400)  # 400 Bad Request


def hello_world3(request):
    return HttpResponse("Hello, World3!")
