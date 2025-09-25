list_of_numbers = [-9, 18, 67, 26, 51, -24, -83, 12, 1]
number_list_two = [-2, -3, -1, 1, -4, 3, 4, 5, 6, 7]


def sort_numbers_asc(list_of_numbers):
    print(
        f"*********ORDENANDO LISTA ASCENDENTE {list_of_numbers}*********")

    for outer_index in range(0, len(list_of_numbers)-1):
        was_ordered = False

        # Iteramos hasta la burbuja, no iteramos nuevamente sobre todos los elementos
        for inner_index in range(0, len(list_of_numbers)-1-outer_index):

            current_number = list_of_numbers[inner_index]
            next_number = list_of_numbers[inner_index+1]

            if next_number < current_number:
                list_of_numbers[inner_index+1] = current_number
                list_of_numbers[inner_index] = next_number
                was_ordered = True
                print(
                    f"Esta es mi lista de números ordenadas de forma ascendente {list_of_numbers}")

        if was_ordered == False:
            print(
                f"Esta es mi lista *FINAL* de números ordenadas de forma ascendente {list_of_numbers}")
            return print("La lista ya esta ordenada no hace falta seguir iterando\n")


sort_numbers_asc(list_of_numbers)