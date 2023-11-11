from ..logic.vitalSign_logic import get_vitalSign_by_pulse, create_vitalSign, create_vitalSign_object

# this function return vitalSign id. If the vitalSign does not exist, then it is created


def get_vitalSign(pulse):
    vitalSign = get_vitalSign_by_pulse(pulse)
    if vitalSign != None:
        return (vitalSign)
    else:
        vitalSign = create_vitalSign_object(pulse)
        return (vitalSign)
