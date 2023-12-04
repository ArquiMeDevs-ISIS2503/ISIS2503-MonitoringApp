from django.shortcuts import render
from .forms import DeviceForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_device import create_device, get_devices, get_deviceSede
from sites.logic.site_logic import get_site_by_name

def device_list(request):
    context = {
        'device_list': []
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

def device_create(request):
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