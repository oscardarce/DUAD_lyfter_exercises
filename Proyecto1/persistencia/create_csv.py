import csv
# from db import db

db = [{"Gastos": "Perreo"}]

# print(db)

def save_in_csv_file():

    print("Ejecutando funcion create csv")

    keys = db.keys()
    values = db.values()

    print(keys, values)

    data_file_name = "data_base.csv"

    with open(data_file_name, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.DictWriter(file, fieldnames=keys)

        csv_writer.writeheader(keys)

        for values in db["Categoria"]:
            csv_writer.writerow(values)

        for values in db["Ingresos"]:
            csv_writer.writerow(values)

        for values in db["Gastos"]:
            csv_writer.writerow(values)


