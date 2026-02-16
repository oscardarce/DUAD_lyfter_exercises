list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

dictionary = {}
counter = 0

for keys in list_a:
    dictionary[keys] = list_b[counter]
    counter = counter + 1


print(dictionary)
