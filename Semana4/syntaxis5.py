# Practica#5
total_grades = 0
grade_counter = 1
current_grade = 0
passed_grades = 0
failed_grades = 0
average_passed = 0
average_failed = 0
overall_average = 0
total_grades = int(input("Por favor ingresa la cantidad de notas "))
while total_grades >= grade_counter:
   while True:
      try:
         grade_counter += 1
         current_grade = int(input("Ingresa tu nota por favor: "))
         if current_grade > 70:
               passed_grades = passed_grades + 1
               average_passed = average_passed + current_grade
         else:
               failed_grades = failed_grades + 1
               average_failed = average_failed + current_grade
         overall_average = overall_average + (current_grade / total_grades)
         break
      except:
         print("Por favor ingresa un número")

if average_passed == 0:
   average_passed = 0
else:
   average_passed = average_passed / passed_grades


if average_failed == 0:
   average_failed = 0
else:
   average_failed = average_failed / failed_grades

print(f"El estudiante tiene {passed_grades} aprobadas")
print(f"El estudiante tiene {failed_grades} reprobadas")
print(f"El promedio de notas aprobadas es de: {average_passed}")
print(f"El promedio de notas aprobadas es de: {average_failed}")
print(
   f"El promedio total final de las notas del estudiante es de {overall_average}")
