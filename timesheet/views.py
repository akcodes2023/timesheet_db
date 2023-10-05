# Create your views here.
# from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TimesheetSerializer
from timesheet.models import Timesheet


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet(request):
    if request.method == 'GET':
        timesheet = Timesheet.objects.all()
        serializer = TimesheetSerializer(timesheet, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet_bydate(request):
    if request.method == 'GET':
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({'error': 'Both start_date and end_date query parameters are required.'}, status=400)

        if start_date_str and not end_date_str:
            return Response({'error': 'Both start date and end date are required for date range filtering.'}, status=400)

        if end_date_str and not start_date_str:
            return Response({'error': 'Both start date and end date are required for date range filtering.'}, status=400)

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response(
                {
                    'error': 'Invalid date format. Use YYYY-MM-DD.'
                },
                status=400
                )

        timesheets = Timesheet.objects.filter(
            date__range=(
                    start_date,
                    end_date
                    )
                )

        # Check if no timesheets are found
        if not timesheets:
            return Response(
                {
                 'error': 'No timesheets found for the specified date range.'
                },
                status=404
                )

        serializer = TimesheetSerializer(timesheets, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_timesheet(request):

    if request.method == 'POST':
        # Handle POST request to create a new employee
        serializer = TimesheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        return Response(serializer.errors, status=400)  # 400 Bad Request

# Create your views here.


def hello_world(request):
    return HttpResponse("Hello, World!")
