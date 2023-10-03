# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from employeeapp.models import Employee


# Create a model serializer
# class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
class EmployeeSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Employee
        fields = '__all__'  # Serialize all fields in the Employee model
