import os
import csv
from persistencia import load_from_csv_file, save_in_csv_file
from db import all_data, data_categories


def test_save_in_csv_file():
    data = [
        {"Categoria": "Comida", "Tipo": "Gasto", "Monto": "2000"},
        {"Categoria": "Salario", "Tipo": "Ingreso", "Monto": "5000"},
    ]

    save_in_csv_file(data)

    # El archivo debe existir
    assert os.path.exists("data_base.csv")

    # El archivo debe tener datos
    with open("data_base.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 2


def test_load_from_csv_file():
    all_data.clear()
    data_categories.clear()

    load_from_csv_file()

    assert len(all_data) > 0

    assert "Comida" in data_categories


def test_load_from_csv_file_no_file():
    if os.path.exists("data_base.csv"):
        os.remove("data_base.csv")

    all_data.clear()
    data_categories.clear()

    # No debe lanzar error
    load_from_csv_file()

    # No se cargó nada
    assert len(all_data) == 0
