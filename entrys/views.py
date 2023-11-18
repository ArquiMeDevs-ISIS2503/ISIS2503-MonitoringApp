from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import EntryForm
from .logic.entry_logic import get_entrys, create_entry
from symptoms.logic.symptom_logic import get_all_symptoms_by_entry
from monitoring.auth0backend import getRole

def entry_list(request):
    role = getRole(request)
    print(role)
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

def entry_create(request):
    role = getRole(request)
    print(role)
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