from ..models import Device

def get_devices():
    queryset = Device.objects.all().order_by('-dateTime')
    return (queryset)

def create_device(form):
    device = form.save()
    device.save()
    return ()

def create_device_object(variable_id, value, unit, place):
    device = Device()
    device.variable = variable_id
    device.value = value
    device.unit = unit
    device.place = place
    device.save()
    return ()