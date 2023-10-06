from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfilesSerializer, UsersSerializer
from profiles.models import Profile
from django.contrib.auth import get_user_model


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_employee(request):
    if request.method == 'GET':
        user = Profile.objects.all()
        serializer = ProfilesSerializer(user, many=True)
        return Response(serializer.data)


User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    if request.method == 'GET':
        id_from_request = request.data.get('id')
        # Extract the id from the request data sent in the GET request body

        if id_from_request:
            try:
                id_from_request = int(id_from_request)
                # Convert the id to an integer
            except ValueError:
                return Response({"error": "Invalid id format"}, status=400)
                # Error response if the id is not a valid integer

            user = User.objects.filter(id=id_from_request).first()
            # Retrieve the user profile based on the id from the request

            if user and user == request.user:
                serializer = UsersSerializer(user)
                return Response(serializer.data)
                # If the id matches the authenticated user's token
                # return the user's details
            else:
                return Response(
                    {
                        "error": "User not found or unauthorized access"
                    },
                    status=403
                    )
                # Return an error response if the id doesn't match,
                # the token user or the user is not found

        return Response(
            {
                "error": "id is required in the request body"
            },
            status=400
            )
        # Error response if the id is missing from the request body


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
