my_list = [4, 3, 6, 1, 7]
first_position_list = my_list[0]
last_position_list = my_list[-1]

my_list[0] = last_position_list

#el índice -1 significa: el último elemento de la lista
my_list[-1] = first_position_list



print(first_position_list)
print(last_position_list)
print(f"{my_list}")
