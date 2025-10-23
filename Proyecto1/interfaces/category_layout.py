import FreeSimpleGUI as sg


def create_category_window():

    category_layout = [
        [sg.Text("Nueva Categoría", font=("Verdana", 14, "bold"))],
        [sg.HorizontalSeparator(p=20, color="red")],
        [sg.Text("Nombre de la categoría:"), sg.Input(key="-CATEGORY_NAME-")],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]

    category_window = sg.Window("Categorías", category_layout, modal=True)

    while True:
        event, values = category_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Guardar":
            sg.popup(f"Categoría agregada: {values['-CATEGORY_NAME-']}"),

        if event == "Cancelar":
            break

    category_window.close()
