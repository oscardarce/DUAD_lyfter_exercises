from menus.main_menu import main_menu


def students_grading_system():
    print("Bienvenido, selecciona una de las siguientes opciones\n")
    while True:
        print("Menú\n"
              "1. Registra un estudiante\n"
              "2. Mostrar estudiantes registrados\n"
              "3. Ver el top 3 de los estudiantes con la mejor nota promedio\n"
              "4. Ver la nota promedio entre las notas de todos los estudiantes\n"
              "5. Exportar todos los datos actuales a un archivo CSV\n"
              "6. Importar los datos de un archivo CSV previamente exportado\n"
              "7. Salir del programa\n")
        try:
            selection = int(input("Selecciona la acción a realizar\n"))
        except ValueError:
            print("Por favor, ingresa un número válido.\n")
            continue

        if selection == 7:
            print("Saliendo del programa")
            break

        try:
            main_menu(selection)
        except Exception as e:
            print(f"Ocurrió un error: {e}\n")


if __name__ == "__main__":
    students_grading_system()
