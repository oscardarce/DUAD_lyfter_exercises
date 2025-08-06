#Practica#1
string = "Hola"
integer = 3
boolean = True
myList = []
myFloat = 0.3333333154194
print(string+string)
print(string+integer)
print(integer+string)
print(myList+myList)
print(string+myList)
print(myFloat+integer)
print(boolean+boolean)

#1. string + string → string “HolaHola”
#2. string + int → TypeError: can only concatenate str (not "int") to str
#3. int + string → TypeError: unsupported operand type(s) for +: 'int' and 'str’
#4. list + list → []
#5. string + list → TypeError: can only concatenate str (not "list") to str
#6. float + int → Float 3.3
#7. bool + bool → 2, quiere decir que `True`debe tener un valor de uno así como `False`de 0 por lo que `True`+`True`= 2