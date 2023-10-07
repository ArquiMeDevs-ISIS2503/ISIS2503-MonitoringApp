from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'name',
            'concentration',
            'amount',
            'type',
            'code',
            'builder',
            'site'
            #'dateExpiration'
        ]
        labels = {
            'name' : 'Name',
            'concentration' : 'Concentration',
            'amount' : 'Amount',
            'type' : 'Type',
            'code' : 'Code',
            'builder' : 'Builder',
            'site' : 'Site'
            #'dateExpiration'
        }