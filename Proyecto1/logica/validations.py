import FreeSimpleGUI as sg

def validate_categories_exist(data_categories):

    if not data_categories:
        sg.popup_error(
            "No hay categorías disponibles.\n"
            "Por favor, crea una categoría antes de registrar movimientos.",
            title="Error - Sin categorías"
        )
        return False
    return True


def validate_movement_fields(amount):

    if not amount:
        sg.popup_error("El monto no puede estar vacío.")
        return False

    try:
        amount = float(amount)
        if amount <= 0:
            sg.popup_error("El monto debe ser mayor a cero.")
            return False
    except ValueError:
        sg.popup_error("El monto debe ser un número válido.")
        return False

    return True


def validate_is_number(input):
    try:
        amount = float(input)
        if amount <= 0:
            sg.popup_error("El monto debe ser mayor a cero.")
            return False
        return True
    except ValueError:
        sg.popup_error("Debe ingresar un número válido.")
        return False
