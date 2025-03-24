from django.shortcuts import render
from .models import Employee

def testmysql(request):
    employees = Employee.objects.all()

    if employees.exists():  # Check if queryset has data
        employee = employees.first()  # Safely get the first employee
        context = {
            'user_ssn': employee.ssn,
            'user_name': employee.lname,
        }
    else:
        context = {  # Provide default values if no employees exist
            'user_ssn': 'N/A',
            'user_name': 'No Employees Found',
        }

    return render(request, 'home.html', context)
