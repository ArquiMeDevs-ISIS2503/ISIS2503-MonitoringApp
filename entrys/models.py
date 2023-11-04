from django.db import models
from diagnostics.models import Diagnostic
from vitalSigns.models import VitalSign


class Entry(models.Model):
    startDate = models.DateTimeField()
    entryDate = models.DateTimeField(auto_now_add=True)
    diagnostic = models.OneToOneField(Diagnostic, on_delete=models.CASCADE, default=None)
    vitalSign = models.OneToOneField(VitalSign, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return '{}'.format(self.entryDate)

