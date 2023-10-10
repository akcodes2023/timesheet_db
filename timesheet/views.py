# Create your views here.
# from django.shortcuts import render
from datetime import date, datetime
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import WorklogSerializer, ProfileSerializer
from timesheet.models import Worklog
from profiles.models import Profile


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet(request):
    if request.method == 'GET':
        timesheet = Worklog.objects.all()
        serializer = WorklogSerializer(timesheet, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet_bydate(request):
    if request.method == 'GET':
        # Check if the date is provided in the query parameters
        current_date = request.GET.get('date')

        if current_date is None:
            return Response({'error': 'The "date" parameter is required.'}, status=400)

        # Convert the date string to a datetime.date object if needed
        if isinstance(current_date, str):
            try:
                current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        # Get a list of approval statuses from the query parameters
        # approval_statuses = request.GET.getlist('approval_status')

        approval_status = request.GET.getlist('approval_status')

        if not approval_status:
            return Response({'error': 'At least one approval status is required.'}, status=400)

        # Define a list of valid approval statuses
        valid_status = ['Submitted', 'Approved', 'Rejected']  # Add more statuses as needed

        # Create a list to store invalid statuses
        invalid_status = []

        # Check if each provided status is valid
        for status in approval_status:
            if status not in valid_status:
                invalid_status.append(status)

        # If there are any invalid statuses, return an error response
        if invalid_status:
            return Response({'error': 'Invalid approval status selected'}, status=400)
            # return Response({'error': f'Invalid approval status: {", ".join(invalid_status)}'}, status=400)

        timesheets = Worklog.objects.filter(
            date=current_date,
            approval_status__in=approval_status
        )

        # Check if no timesheets are found
        if not timesheets:
            return Response(
                {'error': 'No timesheets found for the selected date.'},
                status=404
            )

        # Retrieve the employee details for the timesheet entries
        employee_ids = timesheets.values_list('raised_by_id', flat=True)
        employees = Profile.objects.filter(employee__in=employee_ids)

        # Serialize timesheet data along with employee details
        timesheet_serializer = WorklogSerializer(timesheets, many=True)
        employee_serializer = ProfileSerializer(employees, many=True)

        # Combine the data into a single response
        response_data = {
            'timesheets': timesheet_serializer.data,
            'employees': employee_serializer.data
        }

        return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def timesheet_not_submitted(request):
    if request.method == 'GET':
        # Get the current date
        current_date = request.GET.get('date')

    if current_date is None:
        return Response({'error': 'The "date" parameter is required.'}, status=400)

    # Convert the date string to a datetime.date object if needed
    if isinstance(current_date, str):
        try:
            current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        # Query the Profile model to find employees who haven't submitted a timesheet for the day
        profiles = Profile.objects.exclude(employee__in=Worklog.objects.filter(date=current_date).values('raised_by'))

        # Serialize the profile data
        serializer = ProfileSerializer(profiles, many=True)

        # Return the serialized data as the API response
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet_bydate_range(request):
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

        timesheets = Worklog.objects.filter(
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

        serializer = WorklogSerializer(timesheets, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_timesheet(request):

    if request.method == 'POST':
        # Handle POST request to create a new employee
        serializer = WorklogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        return Response(serializer.errors, status=400)  # 400 Bad Request

# Create your views here.


def hello_world(request):
    return HttpResponse("Hello, World!")
