first_list = ["Hay", "en", "que", "iteración", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

first_list_iteration = []
second_list_iteration = []


for index in range(0, len(first_list)):

    first_list_iteration = first_list[index]
    second_list_iteration = second_list[index]
    print(f"{first_list_iteration} {second_list_iteration}")
