from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import MedicineForm
from .logic.medicine_logic import get_medicines, create_medicine
from monitoring.auth0backend import getRole
from django.contrib.auth.decorators import login_required
import requests
import json

@login_required
def medicine_list(request):
    r = requests.post("http://10.128.0.7:8080/getRole", headers={"Accept":"application/json"}, json=json.dumps(request.user))
    role = r.json()
    print(role)
    if role == "Medico":
        medicines = get_medicines()
        context = {
            'medicine_list': medicines
        }
        return render(request, 'Medicine/medicine.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def medicine_create(request):
    role = getRole(request)
    print(role)
    if role == "Medico":
        if request.method == 'POST':
            form = MedicineForm(request.POST)
            if form.is_valid():
                create_medicine(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created medicine')
                return HttpResponseRedirect(reverse('medicines:medicineCreate'))
            else:
                print(form.errors)
        else:
            form = MedicineForm()

        context = {
            'form': form,
        }
        return render(request, 'Medicine/medicineCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
