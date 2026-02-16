import csv
import json

path = "Semana10\\data\\students_data_base.csv"


def read_csv(students_db):

    with open(path, "r", newline="", encoding="utf-8") as student_csv:
        reader = csv.DictReader(student_csv)

        for student in reader:

            try:
                student["Calificacion"] = json.loads(
                    student["Calificacion"].replace("'", '"'))
            except Exception:
                pass

            else:
                students_db.append(student)
        
        print("Cargaste los datos de los estudiantes")
