from django.db import models
from entrys.models import Entry

class Symptom(models.Model):
    description = models.CharField(max_length=50)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}'.format(self.description)

