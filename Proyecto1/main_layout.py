import FreeSimpleGUI as sg
from db import all_data

# Setear tema
sg.theme("DarkBrown")


def get_data_to_show():

    info_array = []

    for item in all_data:

        if "Gasto" in item:
            info_array.append([item["Gasto"], item["Monto"], "-", "-"])

        elif "Ingreso" in item:
            info_array.append(["-", "-", item["Ingreso"], item["Monto"]])

    return info_array


info_array = get_data_to_show()


# Menú principal
menu_def = [["Cargar", ["CSV", "JSON", "TXT"]],
            ["Exportar", ["CSV", "JSON", "TXT"]]]

headings = ["Gastos", "Monto", "Ingresos", "Monto"]


home_layout = [
    [sg.Menu(menu_def)],
    [sg.Text("Gestor de Finanzas", font=("Verdana", 20, "bold"))],
    [sg.Text("Registro de finanzas", font=("Verdana", 9)),
     sg.HorizontalSeparator(p=20, color="red")],
    [sg.Table(
        values=info_array,
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
