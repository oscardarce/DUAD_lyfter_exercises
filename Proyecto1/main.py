import FreeSimpleGUI as sg
from main_layout import home_layout, get_data_to_show
from interfaces.category_layout import create_category_window
from interfaces.income_layout import create_income_window
from interfaces.expenses_layout import create_expense_window
from persistencia.create_csv import save_in_csv_file
from logica.validations import validate_categories_exist
from persistencia.load_csv import load_from_csv_file
from db import all_data, data_categories


main_window = sg.Window("Finanzas", home_layout)
load_from_csv_file()

while True:
    event, values = main_window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Nueva categoria":
        create_category_window(data_categories)
        new_data = get_data_to_show(all_data)
        main_window['-DATA-'].update(values=new_data)

    elif event == "Ingreso":
        if validate_categories_exist(data_categories):
            create_income_window(all_data, data_categories)
            new_data = get_data_to_show(all_data)
            main_window['-DATA-'].update(values=new_data)

    elif event == "Gasto":
        if validate_categories_exist(data_categories):
            create_expense_window(all_data, data_categories)
            new_data = get_data_to_show(all_data)
            main_window['-DATA-'].update(values=new_data)

    elif event == "CSV":
        save_in_csv_file(all_data)

main_window.close()
