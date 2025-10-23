import FreeSimpleGUI as sg


def create_income_window():

    income_layout = [
        [sg.Text("Registra tu ingreso", font=("Verdana", 9))],
        [sg.Input(key="-INCOME-", default_text='')],
        [sg.HorizontalSeparator(p=20, color="red")],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]

    income_window = sg.Window("Ingreso", income_layout, modal=True)

    while True:
        event, values = income_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Guardar":

            sg.popup(f"Ingreso creado: {values['-INCOME-']}")
            income_window['-INCOME-'].update('')

        if event == "Cancelar":
            break

    income_window.close()
