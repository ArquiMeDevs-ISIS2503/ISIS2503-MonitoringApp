from django.db import models
from sites.models import Site

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    concentration = models.IntegerField(null=True, blank=True, default=None)
    amount = models.IntegerField(null=True, blank=True, default=None)
    type = models.CharField(max_length=50)
    code = models.IntegerField(null=True, blank=True, default=None)
    builder = models.CharField(max_length=50)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=None)
    dateExpiration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

