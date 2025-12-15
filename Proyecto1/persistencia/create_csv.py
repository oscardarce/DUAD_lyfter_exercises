import csv
import FreeSimpleGUI as sg

file_name = "data_base.csv"
path = f"{file_name}"


def save_in_csv_file(data):
    fieldnames = ["Categoria", "Tipo", "Monto"]

    with open(path, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for item in data:
            csv_writer.writerow(item)

    sg.popup(f"Datos guardados: {len(data)}")
