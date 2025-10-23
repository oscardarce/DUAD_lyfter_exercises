import FreeSimpleGUI as sg
from main_layout import home_layout
from interfaces.category_layout import create_category_window
from interfaces.income_layout import create_income_window
from interfaces.expenses_layout import create_expense_window


main_window = sg.Window("Finanzas", home_layout)


# Event Loop para procesar "events" y obtener los "values" de los inputs
while True:
    event, values = main_window.read()

    if event == "Nueva categoria":
        create_category_window()

    if event == "Ingreso":
        create_income_window()

    if event == "Gasto":
        create_expense_window()

    # Procesar el evento del cerrar la ventaja
    if event == sg.WIN_CLOSED:
        break

main_window.close()
