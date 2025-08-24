
def select_back_to_main():
    while True:
        try:
            option = int(input(
                "¿Deseas continuar?\n"
                "1. Sí\n"
                "2. Volver al menú principal\n"
            ))
            if option == 1:
                return True          # seguir iterando
            elif option == 2:
                print("Volviendo al menú principal.\n")
                return False
            else:
                print("Ingresa solo 1 o 2.")
        except ValueError:
            print("Por favor ingresa un número válido.")


def validate_grade(subject):

    while True:
        grade = input(f"Ingresa tu nota de {subject}\n").strip()

        try:
            grade = int(grade)
        except ValueError:
            print("Debes de ingresar un número, no letras.")
            continue

        while grade > 100 or grade < 0:
            grade = float(
                input(f"Por favor ingresa tu nota correctamente de 0 a 100\n"))
            return False
        return grade


def validate_bd(students_db):
    if not students_db:
        print("Aun no tienes registros que mostrar")
        return


def extract_students_data(students_db):
    for all_students in students_db:
        all_students
    return all_students
