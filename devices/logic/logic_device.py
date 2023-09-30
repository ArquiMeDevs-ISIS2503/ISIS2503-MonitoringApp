from ..models import Device

def get_devices():
    queryset = Device.objects.all().order_by('-dateTime')
    return (queryset)

def create_device(form):
    device = form.save()
    device.save()
    return ()

def create_device_object(site_id, active, code, builder, name, amount, type):
    device = Device()
    device.site = site_id
    device.active = active 
    device.code = code
    device.builder = builder
    device.name = name
    device.amount = amount
    device.type = type
    device.save()
    return ()