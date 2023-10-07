from ..models import Medicine


def get_medicines():
    queryset = Medicine.objects.all()
    return (queryset)


def create_medicine(form):
    measurement = form.save() # TODO: PORQUE NOS TOCA CREAR LA VARIABLE DESDE LA PAGINA DE MEDICIONES?
    measurement.save()
    return ()

def create_medicine_object(nameM,concentrationM,amountM,typeM,codeM,builderM,site_id):
    medicine = Medicine()
    medicine.name = nameM
    medicine.concentration = concentrationM
    medicine.amount = amountM
    medicine.type = typeM
    medicine.code = codeM
    medicine.builder = builderM
    medicine.site = site_id
    medicine.save()
    return ()


def get_medicine_by_name(nameM):
    try:
        medicine = Medicine.objects.get(name=nameM)
        return (medicine)
    except:
        medicine = None
        return (medicine)
