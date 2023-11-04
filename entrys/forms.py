from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'startDate',
            'entryDate',
            'diagnostic',
            'vitalSign',
            'symptom'
        ]
        labels = {
            'startDate': 'Start date',
            'entryDate': 'Entry date',
            'diagnostic': 'Diagnostic',
            'vitalSign': 'Vital Sign',
            'symptom': 'Symptom'
        }