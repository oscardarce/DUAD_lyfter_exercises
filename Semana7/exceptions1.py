print("Bienvenido a mi calculadora")


def add(baseNumber, numberToOperate):
    return round(baseNumber + numberToOperate, 2)


def subtract(baseNumber, numberToOperate):
    return round(baseNumber - numberToOperate, 2)


def multiply(baseNumber, numberToOperate):
    return round(baseNumber * numberToOperate, 2)


def divide(baseNumber, numberToOperate):
    return round(baseNumber / numberToOperate, 2)


def numberToString(operation):
    return round(float(operation[1:]), 2)


def validateExitProgram(operation):
    return operation.lower() == 'x'


def typeOfOperation(operation):
    return operation[0]


def calculator():
    print("Ingresa el número que deseas operar precedido del símbolo +, -, *, / o 'x' para salir del programa")

    baseNumber = 0

    while True:
        try:
            operation = input("").strip()

            exitProgram = validateExitProgram(operation)

            if exitProgram:
                print("Saliendo del programa")
                break

            symbol = typeOfOperation(operation)

            numberToOperate = numberToString(operation)

            if symbol not in ["+", "-", "*", "/"]:
                print("Debes ingresar una operación válida: '+', '-', '*', '/'")
                continue

            if symbol == "+":
                baseNumber = add(baseNumber, numberToOperate)
            elif symbol == "-":
                baseNumber = subtract(baseNumber, numberToOperate)
            elif symbol == "*":
                baseNumber = multiply(baseNumber, numberToOperate)
            elif symbol == "/":
                if numberToOperate == 0:
                    print("No puedes dividir entre 0")
                    continue
                baseNumber = divide(baseNumber, numberToOperate)

            print(f"Resultado: {baseNumber}")

        except ValueError:
            print(
                "Debes ingresar un número válido precedido del símbolo de la operación.")
        except IndexError:
            print("Debes ingresar al menos un símbolo de operación y un número.")
        except ZeroDivisionError as error:
            print(f"No puedes dividir entre un número entre 0 {error}")


calculator()
