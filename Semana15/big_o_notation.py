list_of_numbers = [-9, 18, 67, 26, 51, -24, -83, 12, 1, 11, 12, 13]
number_list_two = [-2, -3, -1, 1, -4, 3, 4, 5, 6, 7, 10, 11, 12, 13]
list_three = [-2, -3, -1, 1, -4, 3, 4, 5, 6, 7, 10, 11, 12, 13]

# EJERCICIO  1


def sort_numbers_asc(list_of_numbers):  # FUNCION BIG 0(2^N)

    # Big 0(1) va a ejecutarse el número de elementos de la lista
    print(
        f"*********ORDENANDO LISTA ASCENDENTE {list_of_numbers}*********")

    # Big 0(N)
    for outer_index in range(0, len(list_of_numbers)-1):
        was_ordered = False

        # Big 0(2^n) va a ejecutarse el número de elementos de la lista 1 elevado al número elementos de la lista 2
        for inner_index in range(0, len(list_of_numbers)-1-outer_index):

            # Big 0(1) No es Ciclo o recursivo
            current_number = list_of_numbers[inner_index]
            # Big 0(1) No es Ciclo o recursivo
            next_number = list_of_numbers[inner_index+1]

            # Big 0(1) No es Ciclo o recursivo
            if next_number < current_number:
                list_of_numbers[inner_index+1] = current_number
                list_of_numbers[inner_index] = next_number
                was_ordered = True
                print(
                    f"Esta es mi lista de números ordenadas de forma ascendente {list_of_numbers}")

        # Big 0(1) No es Ciclo o recursivo
        if was_ordered == False:
            print(
                f"Esta es mi lista *FINAL* de números ordenadas de forma ascendente {list_of_numbers}")
            return print("La lista ya esta ordenada no hace falta seguir iterando\n")


# EJERCICIO 2


def print_numbers_times_2(numbers_list):  # FUNCION Big 0(N)

    # Big 0(N)
    for number in numbers_list:
        # Big 0(1) siempre se va a ejecutar 1 vez por cada elemento en la lista
        print(number * 2)


# print_numbers_times_2(list_of_numbers)

##################################################################################

# FUNCION Big 0(2^n)
def check_if_lists_have_an_equal(list_a, list_b):

    # Big 0(N)
    for element_a in list_a:

        # Big 0(2^n) va a ejecutarse el número de elementos de la lista 1 elevado al número elementos de la lista 2
        for element_b in list_b:

            if element_a == element_b:   # Big 0(1) No es Ciclo o recursivo
                return True   # Big 0(1) No es Ciclo o recursivo

    return False   # Big 0(1) No es Ciclo o recursivo

# check_if_lists_have_an_equal(list_of_numbers, number_list_two)

##################################################################################


def print_10_or_less_elements(list_to_print):  # FUNCION # Big 0(N)

    list_len = len(list_to_print)  # Big 0(N)

    # Big 0(N)
    for index in range(min(list_len, 10)):
        print(list_to_print[index])  # Big 0(1) No es Ciclo o recursivo


# print_10_or_less_elements(list_of_numbers)

##################################################################################

def generate_list_trios(list_a, list_b, list_c):  # FUNCION Big 0(3^n)
    result_list = []  # Big 0(1) No es Ciclo o recursivo

    # Big 0(N)
    for element_a in list_a:
        print(f"Iteración {element_a}-----")

        # Big 0(n) va a ejecutarse el número de elementos de la lista 1 elevado al número elementos de la lista 2
        for element_b in list_b:
            print(f"Iteración {element_b}******")

            # Big 0(2^n) va a ejecutarse el número de elementos de la lista 1 elevado màs el nùmero de elementos de la lista 2 y por ultimo cada elemento de la lista 3
            for element_c in list_c:
                print(element_c)
                result_list.append(f'{element_a} {element_b} {element_c}')

    return result_list  # Big 0(1) No es Ciclo o recursivo


# generate_list_trios(list_of_numbers, number_list_two, list_three)
