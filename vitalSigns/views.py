from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VitalSignForm
from .logic.vitalSign_logic import get_vitalSigns, create_vitalSign

def vitalSign_list(request):
    vitalSigns = get_vitalSigns()
    context = {
        'vitalSign_list': vitalSigns
    }
    return render(request, 'VitalSign/vitalSigns.html', context)

def vitalSign_create(request):
    if request.method == 'POST':
        form = VitalSignForm(request.POST)
        if form.is_valid():
            create_vitalSign(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created vitalSign')
            return HttpResponseRedirect(reverse('vitalSignCreate'))
        else:
            print(form.errors)
    else:
        form = VitalSignForm()

    context = {
        'form': form,
    }
    return render(request, 'VitalSign/vitalSignCreate.html', context)