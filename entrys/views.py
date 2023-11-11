from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EntryForm
from .logic.entry_logic import get_entrys, create_entry
from symptoms.logic.symptom_logic import get_all_symptoms_by_entry

def entry_list(request):
    entrys = get_entrys()
    entrySymptoms = {}
    for entry in entrys:
        symptoms = get_all_symptoms_by_entry(entry.id)
        symptomsDescriptions = []
        for symptom in symptoms:
            description = symptom.description
            symptomsDescriptions.append(description)
        entrySymptoms[entry] = symptomsDescriptions
    context = {
        'entry_list': entrys,
        'entry_symptoms' : entrySymptoms
    }
    return render(request, 'Entry/entrys.html', context)

def entry_create(request):
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