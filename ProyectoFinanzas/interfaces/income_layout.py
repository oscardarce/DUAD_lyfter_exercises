import FreeSimpleGUI as sg
from persistencia.csv_save_and_load import save_in_csv_file


def create_income_window(app_instance):

    # Verificar que existan categorías
    category_names = app_instance.get_category_names()

    if not category_names:
        sg.popup_error("Primero debes crear al menos una categoría")
        return

    income_layout = [
        [sg.Text("Registra tu ingreso", font=("Verdana", 15, "bold"))],
        [sg.Text("Monto de tu ingreso", font=("Verdana", 9))],
        [sg.Input(key="-INCOME_AMOUNT-", default_text='')],
        [sg.Text("Ingresa la descripción de tu ingreso", font=("Verdana", 9))],
        [sg.Input(key="-INCOME_DESCRIPTION-", default_text='')],
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

    income_window = sg.Window("Ingreso", income_layout, modal=True)

    while True:
        event, values = income_window.read()

        if event == sg.WIN_CLOSED or event == "Cancelar":
            break

        if event == "Guardar":

            try:
                income_amount = values['-INCOME_AMOUNT-']
                category_selected = values['-CATEGORY-']
                income_description = values['-INCOME_DESCRIPTION-']

                if not category_selected:
                    sg.popup_error("La categoría seleccionada no existe")
                    continue

                if not income_amount:
                    sg.popup_error("El monto debe ser mayor a 0")
                    continue

                if not income_description:
                    sg.popup_error(
                        "Tu movimiento debe tener una descripción")
                    continue

            except ValueError:
                sg.popup_error("El monto debe ser un número válido")
                continue

            try:
                if app_instance.create_income(category_selected, income_amount, income_description):
                    sg.popup(
                        f"Agregaste un nuevo ingreso: {income_amount} en {category_selected}")

                    income_window['-INCOME_AMOUNT-'].update('')
                    income_window['-INCOME_DESCRIPTION-'].update('')

                    save_in_csv_file(app_instance.get_table_data())

            except Exception as e:
                sg.popup_error(f"Error al crear el ingreso: {e}")

    income_window.close()
