import FreeSimpleGUI as sg
from persistencia.csv_save_and_load import save_in_csv_file


def create_expense_window(app_instance):

    # Verificar que existan categorías
    category_names = app_instance.get_category_names()
    if not category_names:
        sg.popup_error("Primero debes crear al menos una categoría")
        return

    expense_layout = [
        [sg.Text("Registra tu gasto", font=("Verdana", 15, "bold"))],
        [sg.Text("Monto de tu gasto", font=("Verdana", 9))],
        [sg.Input(key="-EXPENSE_AMOUNT-", default_text='')],
        [sg.Text("Ingresa la descripción de tu gasto", font=("Verdana", 9))],
        [sg.Input(key="-EXPENSE_DESCRIPTION-", default_text='')],
        [sg.Text("Selecciona una categoría", font=("Verdana", 9))],
        [sg.Combo(
         key="-CATEGORY-",
         values=category_names,
         default_value=category_names[0] if category_names else "",
         readonly=True,
         size=(30, 1)
         )],
        [sg.HorizontalSeparator(p=20, color="red")],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]

    expense_window = sg.Window("Gasto", expense_layout, modal=True)

    while True:
        event, values = expense_window.read()

        if event == sg.WIN_CLOSED or event == "Cancelar":
            break

        if event == "Guardar":

            try:
                expense_amount = float(values['-EXPENSE_AMOUNT-'])
                category_selected = values['-CATEGORY-']
                expense_description = values['-EXPENSE_DESCRIPTION-']

                if expense_amount <= 0:
                    sg.popup_error("El monto debe ser mayor a 0")
                    continue

                if not category_selected:
                    sg.popup_error("La categoría seleccionada no existe")
                    continue

                if not expense_description:
                    sg.popup_error("El movimiento debe tener una descripción")
                    continue

            except ValueError:
                sg.popup_error("El monto debe ser un número válido")
                continue

            try:
                if app_instance.create_expense(category_selected, expense_amount, expense_description):
                    sg.popup(
                        f"Agregaste un nuevo gasto: {expense_amount} en {category_selected}"
                    )
                    expense_window['-EXPENSE_AMOUNT-'].update('')
                    expense_window['-EXPENSE_DESCRIPTION-'].update('')

                    save_in_csv_file(app_instance.get_table_data())

            except Exception as e:
                sg.popup_error(f"Error al crear el gasto: {e}")

    expense_window.close()
