#Practica#4
list_of_user_numbers = []
for i in range(3):
   while True:
      try:
            user_number = int(input("Ingrese un número: "))
            list_of_user_numbers.append(user_number)
            break
      except:
            print("Amigo ingresa un número porfa")
max_number = list_of_user_numbers[i]
for number in list_of_user_numbers:
   if number > max_number:
      max_number = number
print(f"El número más grande es el {max_number}")