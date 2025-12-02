import FreeSimpleGUI as sg
from main_layout import home_layout
from interfaces.category_layout import create_category_window
from interfaces.income_layout import create_income_window
from interfaces.expenses_layout import create_expense_window
from persistencia.create_csv import save_in_csv_file
from main_layout import get_data_to_show

main_window = sg.Window("Finanzas", home_layout)

while True:
    event, values = main_window.read()

    # Exportar Archivos
    # if event == ("Exportar", "CSV"):
    #     save_in_csv_file()

    # if event == ("Exportar", "JSON"):
    #     save_in_json_file()

    # if event == ("Exportar", "TXT"):
    #     save_in_txt_file()

    if event == "Nueva categoria":
        create_category_window()

    if event == "Ingreso":
        create_income_window()
        new_data = get_data_to_show()
        main_window['-DATA-'].update(values=new_data)

    if event == "Gasto":
        create_expense_window()
        new_data = get_data_to_show()
        main_window['-DATA-'].update(values=new_data)

    # Procesar el evento del cerrar la ventaja
    if event == sg.WIN_CLOSED:
        break

main_window.close()
