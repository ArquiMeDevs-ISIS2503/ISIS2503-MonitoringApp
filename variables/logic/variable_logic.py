from ..models import Variable


def get_variables():
    queryset = Variable.objects.all()
    return (queryset)


def create_variable(form):
    measurement = form.save() # TODO: PORQUE NOS TOCA CREAR LA VARIABLE DESDE LA PAGINA DE MEDICIONES?
    measurement.save()
    return ()

def create_variable_object(nombre):
    variable = Variable()
    variable.name = nombre
    variable.save()
    return (variable)


def get_variable_by_name(name):
    try:
        variable = Variable.objects.get(name=name)
        return (variable)
    except:
        variable = None
        return (variable)
