from django.db import models

class VitalSign(models.Model):
    temperature = models.FloatField()
    pulse = models.IntegerField()
    respiratoryFrequency = models.IntegerField()
    arterialPressure = models.FloatField()
    
    def __str__(self):
        return '{}'.format(self.pulse)

