import FreeSimpleGUI as sg
from logica.movimiento import Income
from db import all_data, data_categories


def create_income_window():

    income_layout = [
        [sg.Text("Registra tu ingreso", font=("Verdana", 15, "bold"))],
        [sg.Text("¿Cual es tu ingreso?", font=("Verdana", 9))],
        [sg.Input(key="-INCOME_NAME-", default_text='')],
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

            income_name = values['-INCOME_NAME-'].strip()
            income_amount = values['-INCOME_AMOUNT-'].strip()
            category_selected = values['-CATEGORY-'].strip()

            new_income = Income(income_name, income_amount)
            all_data.append(
                {
                    "Categoria": category_selected,
                    "Ingreso": new_income.income_name,
                    "Monto":  new_income.amount
                }
            )

            print(all_data)

            sg.popup(f"Ingreso creado: {values['-INCOME_NAME-']}")
            income_window['-INCOME_NAME-'].update('')
            income_window['-INCOME_AMOUNT-'].update('')

        if event == "Cancelar":
            break

    income_window.close()
