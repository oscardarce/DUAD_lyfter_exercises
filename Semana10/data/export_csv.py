import csv

students_data_base_file = "students_data_base.csv"
path = f"Semana10\\data\\{students_data_base_file}"


def create_csv(students_db):

    with open(path, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if file.tell() == 0:
            columns = ["Estudiante", "Seccion", "Calificacion"]
            writer.writerow(columns)

        for student in students_db:
            values = list(student.values())
            writer.writerow(values)

        print("Exportaste los datos de los usuarios")
