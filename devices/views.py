from django.shortcuts import render
from .forms import DeviceForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_device import create_device, get_devices

def device_list(request):
    devices = get_devices()
    context = {
        'device_list': devices
    }
    return render(request, 'Device/devices.html', context)

def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            create_device(form)
            messages.add_message(request, messages.SUCCESS, 'Device create successful')
            return HttpResponseRedirect(reverse('deviceCreate'))
        else:
            print(form.errors)
    else:
        form = DeviceForm()

    context = {
        'form': form,
    }

    return render(request, 'Device/deviceCreate.html', context)