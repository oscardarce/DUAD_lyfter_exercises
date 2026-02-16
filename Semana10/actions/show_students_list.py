

def show_students_list(students_db):

    print("\nLista de estudiantes registrados:")

    for all_students in students_db:

        print("*************************************")

        for key, value in all_students.items():
            if key == "Calificacion":
                print(f"{key}:")
                for subject, grade in value.items():
                    print(f"    {subject}: {grade}")
            else:
                print(f"{key}: {value}")

        print("\n")
