from django.shortcuts import render
from .forms import DeviceForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_device import create_device, get_devices, get_deviceSede
from sites.logic.site_logic import get_site_by_name
import requests
import datetime
import json

def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__
    
def device_list(request):
    role = requests.post("http://10.128.0.7:8080/getRole/", headers={"Accept":"application/json"}, json=json.dumps(request.user.social_auth.get(provider="auth0"), default=json_default, sort_keys=True, indent=4)).text
    if role == "Medico":
        context = {
            'device_list': []
        }
        return render(request, 'Device/devices.html', context)
    else:
        return HttpResponse("Unauthorized User")

def device_list_(request):
    devices = get_devices()
    context = {
        'device_list': devices
    }
    return render(request, 'Device/devices.html', context)


def getSede(request):
    if request.method == 'GET':
        sede = request.GET.get('sede')
        sede = get_site_by_name(sede)
        devices = []
        if sede is not None:
            devices = get_deviceSede(sede.id)
        
    context = {
        'device_list': devices,
        'sede': sede
    }
    return render(request, 'Device/devices.html', context)

def device_create1(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            create_device(form)
            messages.add_message(request, messages.SUCCESS, 'Device create successful')
            return HttpResponseRedirect(reverse('devices:deviceCreate'))
        else:
            print(form.errors)
    else:
        form = DeviceForm()

    context = {
        'form': form,
    }

    return render(request, 'Device/deviceCreate.html', context)

# PRINCIPAL
def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            # Suponiendo que el microservicio espera los mismos datos que DeviceForm
            response = requests.post('http://104.197.122.243:8080/create_device/', data=form.cleaned_data)
            print(form.cleaned_data)

            if response.status_code == 201:
                messages.add_message(request, messages.SUCCESS, 'Device create successful')
                return HttpResponseRedirect(reverse('devices:deviceList'))  # Asegúrate de que este es el nombre correcto
            else:
                # Aquí puedes manejar la respuesta no exitosa, como mostrar un error
                messages.add_message(request, messages.ERROR, 'Error creating device')
        else:
            for error in form.errors:
                messages.error(request, f"{error}: {form.errors[error]}")

    else:
        form = DeviceForm()

    context = {
        'form': form,
    }   

    return render(request, 'Device/deviceCreate.html', context)

def create_device1(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            create_device(form)
            messages.add_message(request, messages.SUCCESS, 'Device create successful')
            return HttpResponseRedirect(reverse('devices:deviceCreate'))
        else:
            print(form.errors)
    else:
        form = DeviceForm()

    context = {
        'form': form,
    }

    return render(request, 'Device/create_device.html', context)