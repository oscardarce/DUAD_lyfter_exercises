import FreeSimpleGUI as sg


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
            expense_amount = values['-EXPENSE_AMOUNT-'].strip()
            category_selected = values['-CATEGORY-'].strip()

            try:
                if app_instance.create_expense(category_selected, expense_amount):
                    sg.popup(
                        f"Agregaste un nuevo gasto: {expense_amount} en {category_selected}")
                    expense_window['-EXPENSE_AMOUNT-'].update('')
                    break  # Cerrar ventana después de guardar

            except Exception as e:
                sg.popup_error(f"Error al crear el gasto: {e}")

    expense_window.close()
