from .student_class import Student
from utils.utils import select_back_to_main, validate_grade


def add_student_info(students_db):

    keep_iterating = True
    while keep_iterating:

        student_name = input("Nombre del estudiante:\n").strip().upper()
        while not student_name or len(student_name.strip()) < 3:
            student_name = input(
                "Por favor ingresa el nombre del estudiante:\n")

        student_section_class = input(
            "Sección (ejemplo: *11B*)\n").strip().upper()

        while (
            len(student_section_class.strip().upper()) < 3 or
            len(student_section_class) > 3 or
            not student_section_class[0].isdigit() or
            not student_section_class[1].isdigit() or
            not student_section_class[2].isalpha()
        ):
            student_section_class = input(
                "Ingresa una sección (ejemplo: *11B*)\n")

        spanish_grade = validate_grade("Español")
        english_grade = validate_grade("Ingles")
        history_grade = validate_grade("Sociales")
        science_grade = validate_grade("Ciencias")

        students_db.append(
            Student(
                student_name,
                student_section_class,
                spanish_grade,
                english_grade,
                history_grade,
                science_grade))

        keep_iterating = select_back_to_main()
