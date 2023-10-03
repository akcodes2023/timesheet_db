# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from timesheetapp.models import Timesheet


# Create a model serializer
# class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
class TimesheetSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Timesheet
        fields = '__all__'  # Serialize all fields in the Employee model
