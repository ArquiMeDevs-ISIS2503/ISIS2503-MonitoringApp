from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'startDate',
            'diagnostic',
            'vitalSign',
        ]
        labels = {
            'startDate': 'Start date',
            'diagnostic': 'Diagnostic',
            'vitalSign': 'Vital Sign',
        }