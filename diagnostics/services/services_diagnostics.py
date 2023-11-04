from ..logic.diagnostic_logic import get_diagnostic_by_description, create_diagnostic, create_diagnostic_object

# this function return diagnostic id. If the diagnostic does not exist, then it is created


def get_diagnostic(description):
    diagnostic = get_diagnostic_by_description(description)
    if diagnostic != None:
        return (diagnostic)
    else:
        diagnostic = create_diagnostic_object(description)
        return (diagnostic)
