from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import EntryForm
from .logic.entry_logic import get_entrys, create_entry
from symptoms.logic.symptom_logic import get_all_symptoms_by_entry
from monitoring.auth0backend import getRole
from django.contrib.auth.decorators import login_required
import requests
import datetime
import json

def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__
    
@login_required
def entry_list(request):
    role = requests.post("http://10.128.0.7:8080/getRole/", headers={"Accept":"application/json"}, json=json.dumps(request.user.social_auth.get(provider="auth0"), default=json_default, sort_keys=True, indent=4)).text
    if role == "Medico":
        entrys = get_entrys()
        entrySymptoms = {}
        for entry in entrys:
            symptoms = get_all_symptoms_by_entry(entry.id)
            symptomsDescriptions = []
            for symptom in symptoms:
                description = symptom.description
                symptomsDescriptions.append(description)
            entrySymptoms[entry.id] = symptomsDescriptions
        context = {
            'entry_list': entrys,
            'entry_symptoms' : entrySymptoms
        }
        return render(request, 'Entry/entrys.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def entry_create(request):
    role = requests.post("http://10.128.0.7:8080/getRole/", headers={"Accept":"application/json"}, json=json.dumps(request.user.social_auth.get(provider="auth0"), default=json_default, sort_keys=True, indent=4)).text
    if role == "Medico":
        if request.method == 'POST':
            form = EntryForm(request.POST)
            if form.is_valid():
                create_entry(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created entry')
                return HttpResponseRedirect(reverse('symptoms:symptomCreate'))
            else:
                print(form.errors)
        else:
            form = EntryForm()

        context = {
            'form': form,
        }
        return render(request, 'Entry/entryCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")