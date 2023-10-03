# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from ticketapp.models import Ticket


# Create a model serializer
# class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
class EmployeeSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Ticket
        fields = '__all__'  # Serialize all fields in the Employee model
