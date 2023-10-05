# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from project.models import Project


# Create a model serializer
# class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
class ProjectSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Project
        fields = '__all__'
