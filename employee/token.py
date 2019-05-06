from .models import Employee
import datetime
import json
import time


def jwt_payload_handler(user):
    try:
        employee = Employee.objects.get(user=user)

        return {
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
            'employee_id': employee.pk,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'gender': employee.gender,
            'dni': employee.dni,
            'civil_status': employee.civil_status,
            'adress': employee.address,
        }

    except Employee.DoesNotExist:
        return {
            'employee_id': 0
        }


def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token
    }
