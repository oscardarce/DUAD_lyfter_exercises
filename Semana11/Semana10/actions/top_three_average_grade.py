def top_three_average_grade(students_db):
    print("Top 3 de promedios de estudiante")

    top_tree_students = []

    for student in students_db:

        average_grade = (student.spanish_grade +
                         student.english_grade +
                         student.history_grade +
                         student.science_grade) / 4

        if len(top_tree_students) < 3:
            top_tree_students.append(average_grade)
            print(
                f"--------{student.student_name}: {average_grade}--------")

        else:
            minimum_average = 0

            for grade in range(1, len(top_tree_students)):

                if top_tree_students[grade] < top_tree_students[minimum_average]:
                    minimum_average = grade

            if average_grade > top_tree_students[minimum_average]:
                top_tree_students[minimum_average] = average_grade
                print(
                    f"{student.student_name} tiene una mejor nota que el minimo anterior entra al top 3: {average_grade}")

        sorted_grades = sorted(top_tree_students, reverse=True)

    print(sorted_grades)
