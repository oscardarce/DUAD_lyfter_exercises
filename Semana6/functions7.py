list_of_numbers = [1, 4, 6, 7, 13, 9, 67]


def prime_numbers(numbers):
    prime_numbers_list = []

    for number in numbers:
        if number < 2:
            print(f"{number} no es un número primo")
            continue

        is_prime = True
        # si un número no tiene divisores menores o iguales a su raíz cuadrada, entonces no tiene ninguno en absoluto.
        for divider in range(2, int(number**0.5)+1):
            if number % divider == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers_list.append(number)
        else:
            print(f"{number} no es un número primo")

    print(f"Números primos encontrados: {prime_numbers_list}")


prime_numbers(list_of_numbers)
