from ..logic.medicine_logic import get_medicine_by_name, create_medicine, create_medicine_object

# this function return medicine id. If the medicine does not exist, then it is created


def get_medicine(name):
    medicine = get_medicine_by_name(name)
    if medicine != None:
        return (medicine)
    else:
        medicine = create_medicine_object(name)
        return (medicine)
