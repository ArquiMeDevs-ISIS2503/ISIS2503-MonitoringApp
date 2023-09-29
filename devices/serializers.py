from rest_framework import serializers
from . import models


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'variable', 'value', 'unit', 'place', 'time',)
        model = models.Device