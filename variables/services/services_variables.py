from ..logic.variable_logic import get_variable_by_name, create_variable,create_variable_object

# this function return variable id. If the variable does not exist, then it is created


def get_variable(name):
    variable = get_variable_by_name(name)
    if variable != None:
        return (variable)
    else:
        variable = create_variable_object(name)
        return (variable)
