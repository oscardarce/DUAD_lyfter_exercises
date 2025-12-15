import csv
import FreeSimpleGUI as sg
from db import all_data, data_categories

file_name = "data_base.csv"
path = f"{file_name}"


def load_from_csv_file():

    all_data.clear()

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                all_data.append(row)

                categoria = row.get("Categoria")
                if categoria and categoria not in data_categories:
                    data_categories.append(categoria)

        if len(all_data) > 0:
            print(f"Se cargaron {len(all_data)} registros")

    except FileNotFoundError:
        print("No hay archivo CSV previo")
