from ..models import Device

def get_devices():
    queryset = Device.objects.filter(active=True)
    return (queryset)


def get_deviceSede(sede):
    queryset = Device.objects.filter(active=True,site=sede)
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