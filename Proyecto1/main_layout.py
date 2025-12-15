# main_layout.py
import FreeSimpleGUI as sg
from persistencia.load_csv import load_from_csv_file
from db import all_data

# Setear tema
sg.theme("DarkBrown")

load_from_csv_file()


def get_data_to_show(all_data):
    loaded_data = []

    for item in all_data:
        loaded_data.append([item["Categoria"], item["Tipo"], item["Monto"]])

    return loaded_data


info = get_data_to_show(all_data)

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
        values=info,
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
