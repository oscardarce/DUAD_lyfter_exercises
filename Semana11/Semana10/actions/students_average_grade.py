def students_average_grade(students_db):
    total_of_students = 0
    total_scores = 0
    grades_to_divide = 0

    for student in students_db:
        total_of_students += 1
        grades_to_divide += 4
        total_scores += (student.spanish_grade +
                         student.english_grade +
                         student.history_grade +
                         student.science_grade)

    average_score = total_scores / grades_to_divide

    print(
        f"El total de estudiantes es de: {total_of_students} y el promedio general es de: {average_score}"
    )
