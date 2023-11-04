from ..models import Symptom


def get_symptoms():
    queryset = Symptom.objects.all()
    return (queryset)


def create_symptom(form):
    measurement = form.save() 
    measurement.save()
    return ()

def create_symptom_object(description, entry):
    symptom = Symptom()
    symptom.description = description
    symptom.entry = entry
    symptom.save()
    return (symptom)


def get_symptom_by_description(description):
    try:
        symptom = Symptom.objects.get(description=description)
        return (symptom)
    except:
        symptom = None
        return (symptom)
