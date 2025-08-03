import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def back_to_main():
    try:
        option = int(input(
            "\n1 - Si desea sumar otro número presione 1.\n"
            "2 - Si desea salir al menú principal presione cualquier otra tecla: "))

        if option == 1:
            return True

    except ValueError:
        return False


def add():
    n = 0
    cls()
    keep_operating = True

    while keep_operating:
        try:
            if n == 0:
                number_to_add1 = round(float(
                    input("Ingresa el número que deseas sumar: \n")), 2)

                number_to_add2 = round(float(
                    input("Ingresa cuanto deseas sumar: \n")), 2)

                n = number_to_add1 + number_to_add2
                print(f"Tu resultado es: {n}")

            else:
                number_to_add1 = round(float(
                    input("Ingresa cuanto más deseas sumar: \n")), 2)
                n += number_to_add1
                print(f"Tu resultado es: {n}")
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        keep_operating = back_to_main()

    main()


def subtraction():
    n = 0
    cls()
    keep_operating = True

    while keep_operating:
        try:
            if n == 0:
                number_to_substract1 = round(float(
                    input("Ingresa el número que deseas restar: \n")), 2)

                number_to_substract2 = round(float(
                    input("Ingresa cuanto deseas restarle: \n")), 2)

                n = number_to_substract1 - number_to_substract2
                print(f"Tu resultado es: {n}")

            else:
                print(f"Tu número es {n}")
                number_to_substract1 = round(float(
                    input("Ingresa el número que deseas restar: \n")), 2)
                n -= number_to_substract1
                print(f"Tu resultado es: {n}")

        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        keep_operating = back_to_main()

    main()


def multiply():
    n = 0
    cls()
    keep_operating = True

    while keep_operating:
        try:
            if n == 0:
                number_to_multiply1 = round(float(
                    input("Ingresa el número que deseas multiplicar: \n")), 2)

                number_to_multiply2 = round(float(
                    input("Ingresa cuanto deseas multiplicarle: \n")), 2)

                n = number_to_multiply1 * number_to_multiply2
                print(f"Tu resultado es: {n}")

            else:
                print(f"Tu número es {n}")
                number_to_multiply1 = round(float(
                    input("Ingresa el número que deseas multiplicar: \n")), 2)
                n = n * number_to_multiply1
                print(f"Tu resultado es: {n}")

        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        keep_operating = back_to_main()

    main()


def division():
    n = 0
    cls()
    keep_operating = True

    while keep_operating:
        try:
            if n == 0:
                number_to_divide1 = round(float(
                    input("Ingresa el número que deseas dividir: \n")), 2)

                number_to_divide2 = round(float(
                    input("Ingresa cuanto deseas dividir: \n")), 2)

                n = number_to_divide1 / number_to_divide2
                print(f"Tu resultado es: {n}")

            else:
                print(f"Tu número es {n}")
                number_to_divide1 = round(float(
                    input("Ingresa el número que deseas dividir: \n")), 2)
                n = n / number_to_divide1
                print(f"Tu resultado es: {n}")

        except ValueError:
            print("Por favor ingresa un número válido.")
            continue
        except ZeroDivisionError:
            print("Por favor ingresa un número mayor a cero.")
        keep_operating = back_to_main()

    main()


def calculator_menu(selection):
    match selection:
        case 1:
            return add()
        case 2:
            return subtraction()
        case 3:
            return multiply()
        case 4:
            return division()
        case 5:
            return exit()


def main():
    while True:
        cls()
        try:
            selection_by_user = int(input("Ingresa tu selección: \n"
                                          "1. Suma \n"
                                          "2. Resta \n"
                                          "3. Multiplicación \n"
                                          "4. División \n"
                                          "5. Cerrar programa \n"))
            calculator_menu(selection_by_user)
        except ValueError as ex:
            print(f"Por favor ingresa solo números del 1 al 7.{ex}")


main()
