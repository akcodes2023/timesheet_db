# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from profiles.models import Profile
# from django.contrib.auth.models import User

'''
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined']


'''

# Create a Profile serializer


class UsersSerializer(serializers.ModelSerializer):

    # specify model and fields
    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name', 'last_name']


# Create a User serializer


class ProfilesSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Profile
        fields = '__all__'  # Serialize all fields in the Employee modelzyy
