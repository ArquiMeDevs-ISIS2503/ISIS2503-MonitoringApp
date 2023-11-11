from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import DiagnosticForm
from .logic.diagnostic_logic import get_diagnostics, create_diagnostic

def diagnostic_list(request):
    diagnostics = get_diagnostics()
    context = {
        'diagnostic_list': diagnostics
    }
    return render(request, 'Diagnostic/diagnostics.html', context)

def diagnostic_create(request):
    if request.method == 'POST':
        form = DiagnosticForm(request.POST)
        if form.is_valid():
            create_diagnostic(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created diagnostic')
            return HttpResponseRedirect(reverse('vitalSigns:vitalSigncreate'))
        else:
            print(form.errors)
    else:
        form = DiagnosticForm()

    context = {
        'form': form,
    }
    return render(request, 'Diagnostic/diagnosticCreate.html', context)