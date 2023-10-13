# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from timesheet.models import Worklog
from profiles.models import Profile


# Create a model serializer
class WorklogSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Worklog
        fields = '__all__'  # Serialize all fields in the Employee model


"""
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'employee')
"""


class ProfileSerializer(serializers.ModelSerializer):
    missing_dates = serializers.ListField(
        child=serializers.DateField(),
        read_only=True
        )

    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'employee',
            'missing_dates',
            )
