import csv
import json

students_data_base_file = "students_data_base.csv"
path = f"Semana11\\Semana10\\data\\{students_data_base_file}"


def create_csv(students_db):

    with open(path, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if file.tell() == 0:
            columns = ["Estudiante", "Seccion", "Calificacion"]
            writer.writerow(columns)

        for student in students_db:

            print(student)

            calificacion = json.dumps({
                "Español":  student.spanish_grade,
                "Ingles":   student.english_grade,
                "Historia": student.history_grade,
                "Ciencias": student.science_grade
            }, ensure_ascii=(False))

            values = [
                student.student_name,
                student.student_section_class,
                calificacion
            ]

            writer.writerow(values)

        print("Exportaste los datos de los usuarios")
