from person.models import Person
import datetime
import json
import time


def jwt_payload_handler(user):
    try:
        person = Person.objects.get(user=user)

        return {
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
            'employee_id': person.pk,
            'first_name': person.first_name,
            'last_name': person.last_name,
            'gender': person.gender,
            'dni': person.dni,
            'adress': person.address,
        }

    except Person.DoesNotExist:
        return {
            'employee_id': 0
        }


def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token
    }
