from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MedicineForm
from .logic.medicine_logic import get_medicines, create_medicine

def medicine_list(request):
    medicines = get_medicines()
    context = {
        'medicine_list': medicines
    }
    return render(request, 'Medicine/medicine.html', context)

def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        print(request)
        print(form)
        print(request.data)
        if form.is_valid():
            create_medicine(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created medicine')
            return HttpResponseRedirect(reverse('medicineCreate'))
        else:
            print(form.errors)
    else:
        form = MedicineForm()

    context = {
        'form': form,
    }
    return render(request, 'Medicine/medicineCreate.html', context)