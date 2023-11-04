from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EntryForm
from .logic.entry_logic import get_entrys, create_entry

def entry_list(request):
    entrys = get_entrys()
    context = {
        'entry_list': entrys
    }
    return render(request, 'Entry/entrys.html', context)

def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            create_entry(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created entry')
            return HttpResponseRedirect(reverse('entryCreate'))
        else:
            print(form.errors)
    else:
        form = EntryForm()

    context = {
        'form': form,
    }
    return render(request, 'Entry/entryCreate.html', context)