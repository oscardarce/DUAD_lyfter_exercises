list_of_four_numbers = [4, 6, 2, 29]


def add_numbers_of_the_list(lists_to_add):
    add = 0

    for number in range(len(lists_to_add)):
        add = add + lists_to_add[number]

        print(add)


def main():
    add_numbers_of_the_list(list_of_four_numbers)
    print("Llamado desde la función main")


main()
