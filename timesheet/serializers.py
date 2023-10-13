# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from timesheet.models import Worklog
from profiles.models import Profile


# Create a model serializer
class WorklogSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    # specify model and fields
    class Meta:
        model = Worklog
        fields = (
            'user',
            'title',
            'project',
            'ticket',
            'description',
            'start_date',
            'end_date'
            )
        # fields = '__all__'  # Serialize all fields in the Employee model


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


# Create a model serializer
'''
class GetWorklogSerializer(serializers.ModelSerializer):
    # specify model and fields
    task_name = serializers.CharField(source='title')  # Alias for the 'title' field
    task_description = serializers.CharField(source='effort_description')
    task_link = serializers.CharField(source='ticket')

    class Meta:
        model = Worklog
        # fields = '__all__'  # Serialize all fields in the Employee model
        fields = (
            'task_name',
            'task_description',
            'task_link',
            'start_time',
            'end_time',
        )
'''