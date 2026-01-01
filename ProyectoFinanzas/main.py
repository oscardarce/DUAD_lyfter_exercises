import FreeSimpleGUI as sg
from logica.gestor import GestorFinanzas
from interfaces.category_layout import create_category_window
from interfaces.expenses_layout import create_expense_window
from interfaces.income_layout import create_income_window
from persistencia.csv_save_and_load import save_in_csv_file, load_data_csv

# Setear tema
sg.theme("DarkBrown")

app_instance = GestorFinanzas()

# Cargar datos previos del csv antes de crear el window de main
load_data = load_data_csv(app_instance)

# Obtener los datos para el layout
init_data = app_instance.get_table_data() if load_data > 0 else []

# Crear el layout con los datos ya cargados
menu_def = [
    ['Guardar', 'CSV']
]

headings = ["Categoria", "Tipo", "Monto"]

home_layout = [
    [sg.Menu(menu_def, key="-MENU-")],
    [sg.Text("Gestor de Finanzas", font=("Verdana", 20, "bold"))],
    [sg.Text("Registro de finanzas", font=("Verdana", 9)),
     sg.HorizontalSeparator(p=20, color="red")],
    [sg.Table(
        values=init_data,
        headings=headings,
        max_col_width=135,
        auto_size_columns=True,
        display_row_numbers=True,
        justification="left",
        num_rows=10,
        key="-DATA-",
        row_height=35
    )],
    [sg.Button('Gasto'), sg.Button('Ingreso')],
    [sg.Button('Nueva categoria')],
]

main_window = sg.Window("Finanzas", home_layout)

while True:
    event, values = main_window.read()

    if event == sg.WIN_CLOSED:
        save_in_csv_file(app_instance.get_table_data())
        break

    if event == "Nueva categoria":
        create_category_window(app_instance)
        main_window['-DATA-'].update(values=app_instance.get_table_data())

    elif event == "Ingreso":
        create_income_window(app_instance)
        main_window['-DATA-'].update(values=app_instance.get_table_data())

    elif event == "Gasto":
        create_expense_window(app_instance)
        main_window['-DATA-'].update(values=app_instance.get_table_data())

    elif event == "CSV":
        save_in_csv_file(app_instance.get_table_data())

main_window.close()
