import FreeSimpleGUI as sg


def create_expense_window():

    expense_layout = [
        [sg.Text("Registra tu gasto", font=("Verdana", 9))],
        [sg.Input(key="-INCOME-", default_text='')],
        [sg.HorizontalSeparator(p=20, color="red")],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]

    expense_window = sg.Window("Gasto", expense_layout, modal=True)

    while True:
        event, values = expense_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Guardar":
            sg.popup(f"Ingreso creado: {values['-INCOME-']}")
            expense_window['-INCOME-'].update('')

        if event == "Cancelar":
            break

    expense_window.close()
