import json
from sys import path
from os import environ
import random
import django


site_list = ['Marly', 'Country', 'Santa Fé', 'San Ignacio', 'Policlínica', 'Reina Sofía']
builder_list = ['LG', 'Metronik', 'Samsung', 'Challenger', 'SuperSanaloTodo']
name_list = ['TAC', 'Rayos X', 'MRI', 'Ventilador', 'Respirador', 'Electroalgo']

path.append('monitoring/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')
django.setup()

from devices.logic.logic_device import create_device_object
from sites.services.services_sites import get_site

print('Iniciando la carga de los 10 devices ...')

for i in range(10):    
    site = random.choice(site_list)
    active = random.choice([True, False])
    code = random.randint(100, 1000)
    builder = random.choice(builder_list)
    name = random.choice(name_list)
    amount = random.randint(0, 21)
    type = random.choice(name_list)

    create_device_object(
        site, active, code, builder, name, amount, type)