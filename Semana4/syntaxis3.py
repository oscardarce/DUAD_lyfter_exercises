#Practica#3
import random
while True:
   random_number = random.randint(1,10)
   user_number = int(input("Ingrese un número"))
   if random_number != user_number:
      print(f"No adivinaste el número, era el {random_number}")
   else:
      print(f"Adivinaste el número, bien hecho!")
      break