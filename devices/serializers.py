from rest_framework import serializers
from . import models


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'site', 'active', 'code', 'builder', 'builder', 'name', 'amount', 'type', 'dateMaintainance')
        model = models.Device