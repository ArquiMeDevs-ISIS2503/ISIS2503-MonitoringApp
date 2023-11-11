from django import forms
from .models import VitalSign

class VitalSignForm(forms.ModelForm):
    class Meta:
        model = VitalSign
        fields = [
            'temperature',
            'pulse',
            'respiratoryFrequency',
            'arterialPressure'
        ]
        labels = {
            'temperature': 'Temperature',
            'pulse': 'Pulse',
            'respiratoryFrequency': 'Respiratory frequency',
            'arterialPressure': 'Arterial pressure',
        }