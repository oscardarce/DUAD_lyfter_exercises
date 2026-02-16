

def show_students_list(students_db):

    print("\nLista de estudiantes registrados:")

    for student in students_db:
        print(f"Estudiante: {student.student_name}")
        print(f"Sección: {student.student_section_class}")
        print(
            f"Materías: Ingles: {student.english_grade}, Español: {student.spanish_grade}, Sociales: {student.history_grade}, Ciencias: {student.science_grade}\n")
