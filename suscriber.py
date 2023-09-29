import json
from sys import path
from os import environ
import numpy as np
import django

path.append('monitoring/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')
django.setup()
from devices.logic.logic_device import create_device_object
from variables.services.services_variables import get_variable

print('Iniciando la carga de los 10 devices ...')

def callback(method, body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    topic = method.routing_key.split('.')
    variable = get_variable(topic[2])
    create_device_object(
        variable, payload['value'], payload['unit'], topic[0] + topic[1])

for i in range(10):
    variable = get_variable("medicina")
    value = np.random.randint(0, 20)
    create_device_object(
        variable, value, 'C', 'ML.505')
    