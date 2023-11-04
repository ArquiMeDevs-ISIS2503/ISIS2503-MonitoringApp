from django.db import models

class Diagnostic(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.description)

