def create_student(student_name, student_section_class, spanish_grade, english_grade, history_grade, science_grade, students_db):

    student_name.strip().upper()

    grades = {
        "Estudiante": student_name,
        "Seccion": student_section_class,
        "Calificacion": {
            "Español": spanish_grade,
            "Ingles": english_grade,
            "Historia": history_grade,
            "Ciencias": science_grade
        }
    }

    students_db.append(grades)

    return students_db


if __name__ == "__main__":
    create_student()
