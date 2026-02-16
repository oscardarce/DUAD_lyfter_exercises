import FreeSimpleGUI as sg
from persistencia.csv_save_and_load import save_in_csv_file


def create_category_window(app_instance):

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

            category_value = values['-CATEGORY_NAME-'].strip()

            if app_instance.get_category(category_value):
                sg.popup_error(f"La categoría {category_value} ya existe")
                continue

            if not category_value:
                sg.popup_error(
                    "El nombre de la categoría no puede estar vacío")
                continue

            try:
                if app_instance.create_category(category_value):
                    sg.popup(
                        f"Agregaste una nueva categoría: {category_value}")
                    category_window['-CATEGORY_NAME-'].update('')

            except Exception as e:
                sg.popup_error(f"Error al guardar la categoría: {e}")

        if event == "Cancelar":
            break

    category_window.close()
