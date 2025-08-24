import csv
import json
from actions.student_class import Student

path = "Semana11\\Semana10\\data\\students_data_base.csv"


def read_csv(students_db):

    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for student in reader:
            student_name = student["Estudiante"]
            student_section_class = student["Seccion"]

            # El campo Calificacion viene como string, lo conviertes a dict
            calificacion = json.loads(
                student["Calificacion"].replace("'", '"'))

            spanish_grade = calificacion["Español"]
            english_grade = calificacion["Ingles"]
            history_grade = calificacion["Historia"]
            science_grade = calificacion["Ciencias"]

            students_db.append(
                Student(
                    student_name,
                    student_section_class,
                    spanish_grade,
                    english_grade,
                    history_grade,
                    science_grade))

        print("Cargaste los datos de los estudiantes")
