# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from timesheet.models import Worklog


# Create a model serializer
class WorklogSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Worklog
        fields = '__all__'  # Serialize all fields in the Employee model
