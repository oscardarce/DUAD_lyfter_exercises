import FreeSimpleGUI as sg
from logica.movimiento import Expense
from db import all_data, data_categories


def create_expense_window():

    expense_layout = [
        [sg.Text("Registra tu gasto", font=("Verdana", 15, "bold"))],
        [sg.Text("¿Cual es tu gasto?", font=("Verdana", 9))],
        [sg.Input(key="-EXPENSE_NAME-", default_text='')],
        [sg.Text("Monto de tu gasto", font=("Verdana", 9))],
        [sg.Input(key="-EXPENSE_AMOUNT-", default_text='')],
        [sg.Text("Selecciona una categoría", font=("Verdana", 9))],
        [sg.Combo(
         values=data_categories,
         default_value=data_categories[0],
         readonly=True,
         key="-CATEGORY-",
         size=(30, 1)
         )],        [sg.HorizontalSeparator(p=20, color="red")],
        [sg.Button("Guardar"), sg.Button("Cancelar")],

    ]

    expense_window = sg.Window("Gasto", expense_layout, modal=True)

    while True:
        event, values = expense_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Guardar":

            expense_name = values['-EXPENSE_NAME-'].strip()
            expense_amount = values['-EXPENSE_AMOUNT-'].strip()
            category_selected = values['-CATEGORY-'].strip()

            new_expense = Expense(expense_name, expense_amount)

            all_data.append(
                {
                    "Categoria": category_selected,
                    "Gasto": new_expense.expense_name,
                    "Monto":  new_expense.amount
                }
            )

            print(all_data)

            sg.popup(f"Gasto creado: {values['-EXPENSE_NAME-']}")
            expense_window['-EXPENSE_NAME-'].update('')
            expense_window['-EXPENSE_AMOUNT-'].update('')

        if event == "Cancelar":
            break

    expense_window.close()
