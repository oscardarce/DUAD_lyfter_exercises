
import FreeSimpleGUI as sg
from logica.category import Category
from db import data_categories


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
            category_value = values['-CATEGORY_NAME-'].strip()

            if not category_value:
                sg.popup_error(
                    "El nombre de la categoría no puede estar vacío.")
            else:
                try:
                    new_category = Category(category_value)
                    data_categories.append(new_category.category)

                    sg.popup(
                        f"Agregaste una nueva categoría: {new_category.category}")

                    category_window['-CATEGORY_NAME-'].update('')

                except Exception as e:
                    sg.popup_error(f"Error al guardar la categoría: {e}")

        if event == "Cancelar":
            break

    category_window.close()
