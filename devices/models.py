from django.db import models
from sites.models import Site

class Device(models.Model):
    
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=None)
    active = models.BooleanField()
    code = models.IntegerField(null=True, blank=True, default=None)
    builder = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    amount = models.IntegerField(null=True, blank=True, default=None)
    type = models.CharField(max_length=50)
    dateMaintainance = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)