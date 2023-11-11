from ..models import VitalSign


def get_vitalSigns():
    queryset = VitalSign.objects.all()
    return (queryset)


def create_vitalSign(form):
    measurement = form.save() 
    measurement.save()
    return ()

def create_vitalSign_object(temperatureV, pulseV, respiratoryFrequencyV, arterialPressureV):
    vitalSign = VitalSign()
    vitalSign.temperature = temperatureV
    vitalSign.pulse = pulseV
    vitalSign.respiratoryFrequency = respiratoryFrequencyV
    vitalSign.arterialPressure = arterialPressureV
    vitalSign.save()
    return (vitalSign)


def get_vitalSign_by_pulse(pulse):
    try:
        vitalSign = VitalSign.objects.get(pulse=pulse)
        return (vitalSign)
    except:
        vitalSign = None
        return (vitalSign)
