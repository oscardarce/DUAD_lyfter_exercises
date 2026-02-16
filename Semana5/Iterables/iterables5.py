
my_list = []
counter = 0
higher_list_number = 0

while counter < 9:
    try:
        selected_number = int(input("Por favor ingresa tu número: "))
        my_list.append(counter)
        my_list[counter] = selected_number
        counter += 1
    except:
        print("Tienes que ingresar un número")

for index in range(0, len(my_list)):
    if my_list[index] > higher_list_number:
        higher_list_number = my_list[index]

print(f"Tu lista es {my_list}, y el número más alto es: {higher_list_number}")
