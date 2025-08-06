
my_string = "Pizza con piña"
my_new_string_backwards = ""

for index in range(len(my_string)):
    my_new_string_backwards = my_string[index] + my_new_string_backwards

print(my_new_string_backwards)
