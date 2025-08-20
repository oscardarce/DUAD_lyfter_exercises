

def students_average_grade(students_db):
    total_of_students = 0
    total_scores = 0
    grades_to_divide = 0

    for all_students in students_db:
        total_of_students += 1

        for key, value in all_students.items():
            if key == "Calificacion":
                for subject, score in value.items():
                    total_scores += score
                    grades_to_divide += 1

    average_score = total_scores / grades_to_divide

    print(
        f"El total de estudiantes es de: {total_of_students} y el promedio general es de: {average_score}"
    )
