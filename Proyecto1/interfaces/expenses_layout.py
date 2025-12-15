import FreeSimpleGUI as sg
from logica.movimiento import Movimiento
from logica.validations import validate_movement_fields


def create_expense_window(all_data, data_categories):

    expense_layout = [
        [sg.Text("Registra tu gasto", font=("Verdana", 15, "bold"))],
        [sg.Text("Monto de tu gasto", font=("Verdana", 9))],
        [sg.Input(key="-EXPENSE_AMOUNT-", default_text='')],
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

    expense_window = sg.Window("Gasto", expense_layout, modal=True)

    while True:
        event, values = expense_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Guardar":
            expense_amount = values['-EXPENSE_AMOUNT-'].strip()
            category_selected = values['-CATEGORY-'].strip()

            is_valid = validate_movement_fields(expense_amount)

            if not is_valid:
                continue

            validate_movement_fields(expense_amount)

            try:
                new_expense = Movimiento(expense_amount)

                all_data.append({
                    "Categoria": category_selected,
                    "Tipo": "Gasto",
                    "Monto": new_expense.amount
                })

                print(all_data)

                sg.popup(
                    f"Ingreso creado: {category_selected} : {new_expense.amount}"
                )
                expense_window['-EXPENSE_AMOUNT-'].update('')

            except Exception as e:
                sg.popup_error(f"Error al crear el gasto: {e}")

        if event == "Cancelar":
            break

    expense_window.close()
