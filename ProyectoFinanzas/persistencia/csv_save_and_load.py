import csv
import os
import FreeSimpleGUI as sg

file_name = "data_base.csv"
path = f"{file_name}"


def save_in_csv_file(data):
    fieldnames = ["Categoria", "Tipo", "Monto"]

    with open(path, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in data:
            dictionary = {
                "Categoria": row[0],
                "Tipo": row[1],
                "Monto": row[2]
            }
            csv_writer.writerow(dictionary)

    sg.popup(f"Datos guardados: {len(data)}")


def load_data_csv(gestor_instance):

    if not os.path.exists(path):
        return 0

    loaded_data = 0

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                category_name = row["Categoria"]
                movement_type = row["Tipo"]
                amount = row["Monto"]

                # Crear la categoría si no existe
                if not gestor_instance.get_category(category_name):
                    gestor_instance.create_category(category_name)

                # Crear el movimiento según su tipo
                if movement_type == "Gasto":
                    if gestor_instance.create_expense(category_name, amount):
                        loaded_data += 1
                elif movement_type == "Ingreso":
                    if gestor_instance.create_income(category_name, amount):
                        loaded_data += 1

        return loaded_data

    except Exception as e:
        sg.popup_error(f"Error al cargar datos: {str(e)}")
        return 0
