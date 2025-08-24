from .create_student import create_student
from utils.utils import select_back_to_main, validate_grade


def add_student_info(students_db):

    keep_iterating = True
    while keep_iterating:

        student_name = input("Nombre del estudiante:\n")
        while not student_name or len(student_name.strip()) < 3:
            student_name = input(
                "Por favor ingresa el nombre del estudiante:\n")

        student_section_class = input(
            "Sección (ejemplo: *11B*)\n")

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

        create_student(
            student_name.strip().upper(),
            student_section_class.strip().upper(),
            spanish_grade,
            english_grade,
            history_grade,
            science_grade,
            students_db
        )

        print(f"Haz agregado a {student_name}\n{students_db}")

        keep_iterating = select_back_to_main()


if __name__ == "__main__":
    add_student_info()
