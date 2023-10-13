# Create your views here.
# from django.shortcuts import render
from datetime import date, datetime, timedelta
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import WorklogSerializer, ProfileSerializer
from timesheet.models import Worklog
from profiles.models import Profile
from rest_framework import status
from calendar import Calendar


"""
API to get timesheet of all employees
"""


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet(request):
    if request.method == 'GET':
        timesheet = Worklog.objects.all()
        serializer = WorklogSerializer(timesheet, many=True)
        return Response(serializer.data)


"""
API will return the details of the timesheet
based on selected date range and employee
"""


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet_bydate_range(request):
    if request.method == 'GET':
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')
        raised_by_str = request.GET.get('raised_by')

        # Check if start_date, end_date, and raised_by are not provided in the query string
        if not (start_date_str and end_date_str and raised_by_str):
            # If not provided in the query string, check the request data
            start_date_str = request.data.get('start_date')
            end_date_str = request.data.get('end_date')
            raised_by_str = request.data.get('raised_by')

        # Check if start_date, end_date, and raised_by are not provided
        if not (start_date_str and end_date_str and raised_by_str):
            return Response({'error': 'All of start_date, end_date, and raised_by parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        timesheets = Worklog.objects.filter(
            date__range=(start_date, end_date),
            raised_by__employee=raised_by_str  # Replace 'employee_id' with the actual field name if needed
        )

        # Check if no records were found
        if not timesheets:
            return Response({'message': 'No timesheets found for the specified date range and raised_by.'}, status=status.HTTP_200_OK)

        # Retrieved the employee details for the timesheet entries
        employee_ids = timesheets.values_list('raised_by', flat=True)
        employees = Profile.objects.filter(employee__in=employee_ids)

        # Serialized the timesheet data along with employee details
        event_serializer = WorklogSerializer(timesheets, many=True)
        profile_serializer = ProfileSerializer(employees, many=True)

        # Combine the data into a single response
        response_data = {
            'timesheets': event_serializer.data,
            'employees': profile_serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)


"""
 API to get the timesheet of the employees who have not submitted the timesheet
 for the selected date range
"""


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def timesheet_not_submitted(request):
    if request.method == 'GET':
        # Get the start_date and end_date from the query parameters
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')

        # If not provided in the query string, check the request data
        if not (start_date_str and end_date_str):
            start_date_str = request.data.get('start_date')
            end_date_str = request.data.get('end_date')

        # Check if both start_date and end_date are provided
        if not (start_date_str and end_date_str):
            return Response({'error': 'Both "start_date" and "end_date" parameters are required.'}, status=400)

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        # Query the Profile model to find employees who haven't submitted a timesheet for the selected date range
        profiles = Profile.objects.exclude(
            employee__in=Worklog.objects.filter(date__range=(start_date, end_date)).values('raised_by')
        )

        # Create a list to store employee profiles with missing dates and count
        data = []

        for profile in profiles:
            # Query for all the dates within the date range
            all_dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

            # Query for the list of dates when the employee hasn't submitted a timesheet
            missing_dates = list(set(all_dates) - set(Worklog.objects.filter(raised_by=profile.employee, date__in=all_dates).values_list('date', flat=True)))

            excluded_dates = []
            for missing_date in missing_dates:
                if missing_date.weekday() == 6:  # Check if it's a Sunday (Monday is 0 and Sunday is 6)
                    continue  # Exclude Sundays
                if missing_date.weekday() == 5:  # Check if it's a Saturday (Monday is 0 and Sunday is 6)
                    month_start = missing_date.replace(day=1)
                    if 8 <= (missing_date - month_start).days <= 14:
                        continue  # Exclude 2nd Saturdays
                    if 22 <= (missing_date - month_start).days <= 28:
                        continue  # Exclude 4th Saturdays
                excluded_dates.append(missing_date)

            # Sort the missing_dates to ensure they are in order
            # missing_dates = sorted(missing_dates)
            excluded_dates = sorted(excluded_dates)

            # Include the count of missing dates
            # missing_dates_count = len(missing_dates)

            # Include the count of excluded dates
            excluded_dates_count = len(excluded_dates)

            # Serialize the profile data
            profile_data = ProfileSerializer(profile).data

            # Include the list of missing dates and count in the profile data
            # profile_data['missing_dates'] = [date.strftime('%Y-%m-%d') for date in missing_dates]
            # profile_data['missing_dates_count'] = missing_dates_count

            # Include the list of excluded dates and count in the profile data
            profile_data['excluded_dates'] = [date.strftime('%Y-%m-%d') for date in excluded_dates]
            profile_data['excluded_dates_count'] = excluded_dates_count

            data.append(profile_data)

        return Response(data)



"""
API will return timesheet and profile details based
on either of the below selection
1) selected date
2) selected approval status
3) Both date and spproval_status
"""


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet_bydate(request):
    if request.method == 'GET':
        # Check if date and status are provided in the query parameters
        current_date = request.GET.get('date')
        status = request.GET.getlist('status')

        # Check if both date and status are provided
        if current_date and status:
            # Convert the date string to a datetime.date object if needed
            if isinstance(current_date, str):
                try:
                    current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
                except ValueError:
                    return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

            # Define a list of valid approval statuses
            valid_status = ['Submitted', 'Approved', 'Rejected']  # Add more statuses as needed

            # Create a list to store invalid statuses
            invalid_status = []

            # Check if each provided status is valid
            for status in status:
                if status not in valid_status:
                    invalid_status.append(status)

            # If there are any invalid statuses, return an error response
            if invalid_status:
                return Response({'error': 'Invalid approval status selected'}, status=400)

            timesheets = Worklog.objects.filter(
                date=current_date,
                status__in=status
            )
        elif current_date:
            # If only date is provided, filter based on the date
            # Convert the date string to a datetime.date object if needed
            if isinstance(current_date, str):
                try:
                    current_date = datetime.strptime(current_date, '%Y-%m-%d').date()  # Correct format: '%Y-%m-%d'
                except ValueError:
                    return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

            timesheets = Worklog.objects.filter(date=current_date)
        elif status:
            # If only approval_status is provided, filter based on the approval status
            # Define a list of valid approval statuses
            valid_status = ['Submitted', 'Approved', 'Rejected']  # Add more statuses as needed

            # Create a list to store invalid statuses
            invalid_status = []

            # Check if each provided status is valid
            for status in status:
                if status not in valid_status:
                    invalid_status.append(status)

            # If there are any invalid statuses, return an error response
            if invalid_status:
                return Response({'error': 'Invalid approval status selected'}, status=400)

            timesheets = Worklog.objects.filter(status__in=status)
        else:
            # If neither date nor approval_status is provided, return an error message
            return Response({'error': 'Date or Approval_status or both is required.'}, status=400)

        # Check if no timesheets are found
        if not timesheets:
            return Response({'error': 'No timesheets found for the selected date and approval status.'}, status=404)

        # Retrieved the employee details for the timesheet entries
        employee_ids = timesheets.values_list('raised_by_id', flat=True)
        employees = Profile.objects.filter(employee__in=employee_ids)

        # Serialized the timesheet data along with employee details
        timesheet_serializer = WorklogSerializer(timesheets, many=True)
        employee_serializer = ProfileSerializer(employees, many=True)

        # Combine the data into a single response
        response_data = {
            'timesheets': timesheet_serializer.data,
            'employees': employee_serializer.data
        }

        return Response(response_data)




"""
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
"""

"""
API to get the timesheet details of the employees based on the selected date range



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
"""




"""
API to create timesheet
"""


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
