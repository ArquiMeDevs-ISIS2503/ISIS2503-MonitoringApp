import json
from sys import path
from os import environ
import random
import django
from devices.logic.logic_device import create_device_object
from sites.services.services_sites import get_site

path.append('monitoring/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')
django.setup()


print('Iniciando la carga de los 10 devices ...')

def callback(method, body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    topic = method.routing_key.split('.')
    variable = get_site(topic[2])
    create_device_object(
        variable, payload['value'], payload['unit'], topic[0] + topic[1])

for i in range(10):    
    site = get_site("marly")
    value = random.randint(0, 20)
    create_device_object(
        site, value, 'C', 'ML.505')