import csv

file_name = "video_games_info2.csv"


def video_games_csv(file_name):
    keep_iterating = True

    with open(file_name, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file, delimiter="\t")

        if file.tell() == 0:
            columns = ["Nombre", "Genero", "Desarrollador", "ESRB"]
            writer.writerow(columns)

        while keep_iterating:
            name = input(
                "Ingresa por favor el nombre del video juego\n").strip()
            while not name:
                name = input(
                    "Ingresa por favor el nombre del video juego\n").strip()

            genre = input(
                "Ingresa por favor el género del video juego\n")
            while not genre:
                genre = input(
                    "Ingresa por favor el género del video juego\n")

            developer = input(
                "Ingresa por favor el desarrollador del video juego\n")
            while not developer:
                developer = input(
                    "Ingresa por favor el desarrollador del video juego\n")

            esrb = input(
                "Ingresa por favor su clasificación ESRB\n")
            while not esrb:
                esrb = input(
                    "Ingresa por favor su clasificación ESRB\n")

            rows = [name, genre, developer, esrb]

            writer.writerow(rows)

            while keep_iterating:
                try:
                    validate_continue = int(
                        input("Para continuar seleciona 1 o 2 para salir\n"))
                    if validate_continue == 2:
                        keep_iterating = False
                        print("Saliendo del programa")
                        break
                    if validate_continue == 1:
                        print("Continuemos agregando videojuegos.")
                        break
                except ValueError:
                    print("Ingresa un opción valida.")


video_games_csv(file_name)
