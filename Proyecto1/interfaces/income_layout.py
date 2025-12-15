import FreeSimpleGUI as sg
from logica.movimiento import Movimiento
from logica.validations import validate_movement_fields


def create_income_window(all_data, data_categories):

    income_layout = [
        [sg.Text("Registra el monto del ingreso",
                 font=("Verdana", 15, "bold"))],
        [sg.Text("Monto de tu ingreso", font=("Verdana", 9))],
        [sg.Input(key="-INCOME_AMOUNT-", default_text='')],
        [sg.Text("Selecciona una categoría", font=("Verdana", 9))],
        [sg.Combo(
            values=data_categories,
            default_value=data_categories[0],
            readonly=True,
            key="-CATEGORY-",
            size=(30, 1)
        )],
        [sg.HorizontalSeparator(p=20, color="red")],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]

    income_window = sg.Window("Ingreso", income_layout, modal=True)

    while True:
        event, values = income_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Guardar":

            income_amount = values['-INCOME_AMOUNT-'].strip()
            category_selected = values['-CATEGORY-'].strip()

            is_valid = validate_movement_fields(income_amount)

            if not is_valid:
                continue

            try:
                new_income = Movimiento(income_amount)

                all_data.append(
                    {
                        "Categoria": category_selected,
                        "Tipo": "Ingreso",
                        "Monto":  new_income.amount
                    }
                )

                print(all_data)

                sg.popup(
                    f"Gasto creado: {category_selected} : {new_income.amount}")
                income_window['-INCOME_AMOUNT-'].update('')
            except Exception as e:
                sg.popup_error(f"Error al crear el gasto: {e}")

        if event == "Cancelar":
            break

    income_window.close()
