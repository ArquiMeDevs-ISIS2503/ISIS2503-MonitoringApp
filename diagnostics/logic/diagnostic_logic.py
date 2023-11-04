from ..models import Diagnostic


def get_diagnostics():
    queryset = Diagnostic.objects.all()
    return (queryset)


def create_diagnostic(form):
    measurement = form.save() # TODO: PORQUE NOS TOCA CREAR LA VARIABLE DESDE LA PAGINA DE MEDICIONES?
    measurement.save()
    return ()

def create_diagnostic_object(description):
    diagnostic = Diagnostic()
    diagnostic.description = description
    diagnostic.save()
    return (diagnostic)


def get_diagnostic_by_description(description):
    try:
        diagnostic = Diagnostic.objects.get(description=description)
        return (diagnostic)
    except:
        diagnostic = None
        return (diagnostic)
