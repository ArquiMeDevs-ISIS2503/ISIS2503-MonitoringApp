from ..logic.symptom_logic import get_symptom_by_description, create_symptom, create_symptom_object

# this function return symptom id. If the symptom does not exist, then it is created


def get_symptom(description):
    symptom = get_symptom_by_description(description)
    if symptom != None:
        return (symptom)
    else:
        symptom = create_symptom_object(description)
        return (symptom)
