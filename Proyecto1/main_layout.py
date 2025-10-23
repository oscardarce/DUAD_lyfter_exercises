import FreeSimpleGUI as sg

# Setear tema
sg.theme("DarkBrown")

# Menú principal
menu_def = [["Cargar", ["CSV", "JSON", "FTXT"]],
            ["Exportar", ["CSV", "JSON", "FTXT"]]]

headings = ["Gastos", "Monto", "Ingresos", "Monto"]

info_array = [["Pago de pañaes", 200, "Salario", 300],
              ["Medicinas", 500, "Venta de repostería", 500]]


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
