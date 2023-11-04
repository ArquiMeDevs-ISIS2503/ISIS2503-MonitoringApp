from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import DiagnosticForm
from .logic.symptom_logic import get_symptoms, create_symptom

def symptom_list(request):
    symptoms = get_symptoms()
    context = {
        'symptom_list': symptoms
    }
    return render(request, 'Diagnostic/symptoms.html', context)

def symptom_create(request):
    if request.method == 'POST':
        form = DiagnosticForm(request.POST)
        if form.is_valid():
            create_symptom(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created symptom')
            return HttpResponseRedirect(reverse('symptomCreate'))
        else:
            print(form.errors)
    else:
        form = DiagnosticForm()

    context = {
        'form': form,
    }
    return render(request, 'Diagnostic/symptomCreate.html', context)