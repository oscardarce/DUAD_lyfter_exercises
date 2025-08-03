my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_new_list = []

for index, value in enumerate(my_list):
    if value % 2 == 0:
        my_new_list.append(value)

print(f"{my_new_list}")
