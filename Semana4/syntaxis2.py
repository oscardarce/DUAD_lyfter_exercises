#Practica#2

user_name = input("Ingrese su nombre")
user_lastname = input("Ingrese su apellido")
user_age = int(input("Ingrese su edad"))
if user_age < 3:
   print(f"Qué lindo bebé {user_name} {user_lastname} tiene menos de 3 años, tiene: {user_age}")
elif user_age >= 3 and user_age < 10:
   print(f"{user_name} {user_lastname} ya es un guila, tiene: {user_age}")
elif user_age >= 10 and user_age < 12:
   print(f"{user_name} {user_lastname} es un preadolescente, tiene : {user_age}")
elif user_age >= 12 and user_age < 18:
   print(f"{user_name} {user_lastname} es un adolescente, tiene : {user_age}")
elif user_age >= 18 and user_age < 30:
   print(f"{user_name} {user_lastname} es un adulto joven, tiene : {user_age}")
elif user_age >= 30 and user_age < 65:
   print(f"{user_name} {user_lastname} es un adulto, tiene : {user_age}")
elif user_age >= 65:
   print(f"{user_name} {user_lastname} es un viejito, tiene : {user_age}")