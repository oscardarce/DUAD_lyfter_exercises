global_scope_variable = 20


def greet():
    local_scope_variable = "Hola al que lee esto."
    print(local_scope_variable)


def main():
    # local_scope_variable is not defined (La variable existe unicamente en la función greet())
    practice2_1 = f"{local_scope_variable}, estoy realizando el punto 2.1 de la practica"

    # global_scope_variable = 200
    practice2_2 = f"{global_scope_variable * 10}"

    print(practice2_1)
    print(practice2_2)


main()
