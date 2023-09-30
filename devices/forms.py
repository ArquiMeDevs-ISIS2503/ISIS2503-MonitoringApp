from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'site',
            'active',
            'code',
            'builder',
            'name',
            'amount',
            'type'
            #'dateMaintainance',
            #'dateTime',
        ]

        labels = {
            'site' : 'Site',
            'active' : 'Active',
            'code' : 'Code',
            'builder' : 'Builder',
            'name' : 'Name',
            'amount' : 'Amount',
            'type' : 'Type'
            #'dateTime' : 'Date Time',
        }
